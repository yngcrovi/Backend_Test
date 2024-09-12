from repository.table_orm.product import Product
from .product_service import ProductService

table = Product

dict_operation = {

}

dict_column_table = {
    'name_product': Product.name_product,
    'type_product': Product.type_product,
    'calories': Product.calories,
    'protein': Product.protein,
    'fat': Product.fat,
    'carbohydrates': Product.carbohydrates,
    'price': Product.price
}

def operation_filter(filter_column, operator, value_filter):
    table = dict_column_table[filter_column]
    if operator == '=' and value_filter:
        return [table == value_filter]
    elif operator == '!=' and value_filter:
        return [table != value_filter]
    elif operator == '>' and value_filter:
        return [table > value_filter]
    elif operator == '>=' and value_filter:
        return [table >= value_filter]
    elif operator == '<' and value_filter:
        return [table < value_filter]
    elif operator == '<=' and value_filter:
        return [table <= value_filter]
    else:
        return []