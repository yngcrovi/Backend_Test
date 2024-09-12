from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from repository.db_repo.service.product_service.product_service import product_service
from repository.db_repo.service.product_service.product_filter_model import operation_filter

route = APIRouter(
    prefix='/product',
    tags=['Product']
)

class ProductData(BaseModel):
    name_product: str
    type_product: str
    calories: int
    protein: float
    fat: float
    carbohydrates: float
    price: int

class FilterProduct(BaseModel):
    type_product: list[str] = None
    operation: dict = None
    calories: int = None
    protein: float = None
    fat: float = None
    carbohydrates: float = None
    price: int = None

class ProductDel(BaseModel):
    name_product: str

class OldProduct(BaseModel):
    old_product: list



@route.get("/get")
async def get() -> JSONResponse:
    product = await product_service.select_product()
    all_product = []
    if type(product) != list:
        help_dict: dict = product.model_dump()
        keys = list(help_dict)
        for j in keys:
            all_product.append(help_dict[j])
    else:
        for i in range(len(product)):
            help_dict: dict = product[i].model_dump()
            keys = list(help_dict)
            all_product.append([])
            for j in keys:
                all_product[i].append(help_dict[j])
    response = JSONResponse(
        content={
            'all_product': all_product
        }, 
        status_code=200
    )
    return response

@route.post("/insert")
async def insert(
    product_data: ProductData,
) -> JSONResponse:
    product_data = product_data.model_dump()
    await product_service.insert_product(product_data)
    response = JSONResponse(
        content = {
            }, 
            status_code = 200
        )
    return response

@route.delete("/delete")
async def delete(
    product_data: ProductDel,
) -> JSONResponse:
    product_data = product_data.model_dump()
    await product_service.delete_product(product_data)
    response = JSONResponse(
        content = {
            }, 
            status_code = 200
        )
    return response

@route.put("/update")
async def update(
    new_product: ProductData,
    old_product: OldProduct
) -> JSONResponse:
    new_product = new_product.model_dump()
    list_new_product = list(new_product.values())
    keys_new_product = list(new_product.keys())
    old_product = old_product.old_product
    dict_new_product = {}
    dict_old_product = {}
    for i in range(len(list_new_product)):
        if list_new_product[i] != old_product[i]:
            dict_new_product[keys_new_product[i]] = list_new_product[i]
        else:
            dict_old_product[keys_new_product[i]] = old_product[i]
    await product_service.update_product(dict_new_product, dict_old_product)
    response = JSONResponse(
        content = {
            }, 
            status_code = 200
        )
    return response

@route.post("/filter")
async def filter(
    filter_data: FilterProduct,
):
    filter_data = filter_data.model_dump()
    list_filter = []
    list_filter.append(filter_data['type_product'])
    if filter_data['calories']:
        list_filter.append(operation_filter('calories', filter_data['operation']['calories'], filter_data['calories']))
    else:
        list_filter.append([])
    if filter_data['protein']:
        list_filter.append(operation_filter('protein', filter_data['operation']['protein'], filter_data['protein']))
    else:
        list_filter.append([])
    if filter_data['fat']:
        list_filter.append(operation_filter('fat', filter_data['operation']['fat'], filter_data['fat']))
    else:
        list_filter.append([])
    if filter_data['carbohydrates']:
        list_filter.append(operation_filter('carbohydrates', filter_data['operation']['carbohydrates'], filter_data['carbohydrates']))
    else:
        list_filter.append([])
    if filter_data['price']:
        list_filter.append(operation_filter('price', filter_data['operation']['price'], filter_data['price']))
    else:
        list_filter.append([])
    query = await product_service.filter_product(list_filter)
    all_product = []
    if type(query) != list:
        query = query.model_dump()
        del query['id']
        keys = list(query)
        for i in keys:
            all_product.append(query[i])
    else:
        for i in range(len(query)):
            help_dict: dict = query[i].model_dump()
            del help_dict['id']
            keys = list(help_dict)
            all_product.append([])
            for j in keys:
                all_product[i].append(help_dict[j])
    return all_product

@route.get("/get_param")
async def get_param() -> JSONResponse:
    name_product = []
    type_product = []
    product_data = await product_service.get_all()
    if type(product_data) != list:
        help_dict = product_data.model_dump()
        if help_dict['type_product'] not in type_product:
            type_product.append(help_dict['type_product'])
        name_product.append(help_dict['name_product'])
    else:
        for i in range(len(product_data)):
            help_dict = product_data[i].model_dump()
            if help_dict['type_product'] not in type_product:
                type_product.append(help_dict['type_product'])
            name_product.append(help_dict['name_product'])
    response = JSONResponse(
        content = {
            'name_product': name_product,
            'type_product': type_product
            }, 
            status_code = 200
        )
    return response