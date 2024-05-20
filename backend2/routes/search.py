from middleware.weaviate import weaviate_middleware_search
from fastapi import Depends, APIRouter, Request, Form
from routes.auth import get_current_user
from models.user import User
from fastapi import HTTPException

router = APIRouter(
    prefix="/search",
    tags=["searches"],
    responses={404: {"description": "Not found"}}
)


@router.get("/test", response_model=str)
async def read_item():
    return "Hello World"

@router.post("/search_query", response_model=str)
def search_query(request,user:User = Depends(get_current_user)):
    try:
        if not user:
            raise HTTPException(status_code=401,detail="Unauthorised")
        search_result = weaviate_middleware_search(request)
    except Exception as e:
        raise Exception(e)
    return search_result