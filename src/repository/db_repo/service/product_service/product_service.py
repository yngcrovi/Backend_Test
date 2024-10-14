from repository.db_repo.postgre_repo import PostgreSQLRepository
from repository.table_orm.product import Product
from ..dto.product_dto import ProductGetDTO, ProductIdDTO, ProductGetWithIdDTO
from sqlalchemy import select, case, literal


class ProductService(PostgreSQLRepository): 

    def __init__(self, table) -> None:
        self.table = table

    async def select_product(self, filter_data: dict = None, dto = ProductGetDTO) -> ProductGetDTO:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(dto, res)
        return result_dto
    
    async def insert_product(self, insert_data: dict | list) -> Product:
        value = await self.insert_data(insert_data)
        return value
    
    async def delete_product(self, delete_data: dict) -> None:
        result = await self.select_product(delete_data, ProductIdDTO)
        await self.delete_data(result.id)

    async def update_product(self, new_product, old_product):
        result = await self.select_product(old_product, ProductIdDTO)
        await self.update_data(result.id, new_product)

    async def filter_product(self, filter_data: list[list]):
        async with self.asf() as session:
            query = (
                select(self.table)
                .filter(
                    case(
                        (len(filter_data[0]) != 0, self.table.type_product.in_(filter_data[0])),
                        else_=literal(True)
                    ))
                .filter(*filter_data[1])
                .filter(*filter_data[2])
                .filter(*filter_data[3])
                .filter(*filter_data[4])
                .filter(*filter_data[5])
                )
            result = await session.execute(query)
            res = result.scalars().all()
            result_dto = self.get_dto_form(ProductGetWithIdDTO, res)
            return result_dto
    
    async def get_all(self):
        async with self.asf() as session:
            query = select(self.table)
            result = await session.execute(query)
            res = result.scalars().all()
            result_dto = self.get_dto_form(ProductGetDTO, res)
            return result_dto
        
product_service = ProductService(Product)
