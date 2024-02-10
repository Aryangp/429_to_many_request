from middleware.weaviate import weaviate_middleware_search

def search_query(request):
    try:
        search_result = weaviate_middleware_search(request)
    except Exception as e:
        raise Exception(e)
    return search_result