from app.utils import weaviate


def search_controller(query,filters):
    # for current purpose we are only creating embeding of query , after testing we use filters
    try:
        search_result = weaviate.weaviate_search(query, filters)
    except Exception as e:
        raise Exception(e)
    
    return search_result


def add_data_controller(data):
    # for current purpose we are only creating embeding of query , after testing we use filters
    try:
       res= weaviate.add_data(data)
    except Exception as e:
        raise Exception(e)
    
    return "Data added successfully"
