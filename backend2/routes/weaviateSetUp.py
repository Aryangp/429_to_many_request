from middleware.weaviate import weaviate_middleware_add_data, weaviate_create_schema
from fastapi import Depends, APIRouter, Request, Form


router = APIRouter(
    prefix="/setup",
    tags=["setups"],
    responses={404: {"description": "Not found"}}
)


@router.post("/schema", response_model=str)
def weaviate_set_up_schema(request):
    try:
        data=request.get_json()
        className=data['className']
        properties=data['properties']
        creation_result = weaviate_create_schema(className, properties=properties)
        return creation_result
    except Exception as e:
        raise Exception(e)


@router.post("/add_data", response_model=str)
def weaviate_add_data(request):
    try:
        add_result = weaviate_middleware_add_data(request)
        return add_result
    except Exception as e:
        raise Exception(e)