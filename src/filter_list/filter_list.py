from src.repository.db_repo.service.product_service.product_filter_model import operation_filter

def filter_list(filter_data):
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
    return list_filter