from middleware.weaviate import weaviate_middleware_search
from fastapi import Depends, APIRouter, Request, Form
from routes.auth import get_current_user
from models.user import User
from fastapi import HTTPException
from typing import Tuple, Annotated
from models.user import User, WeaviateData
from sqlalchemy.orm import Session
from middleware.pasql_mid import SessionLocal
from middleware.weaviate import weaviate_filter_price
from middleware.jwt_auth import get_current_user
import json

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/search",
    tags=["searches"],
    responses={404: {"description": "Not found"}}
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/test", response_model=str)
async def read_item():
    return "Hello World"

@router.post("/search_query", response_model=str)
async def search_query(request:Request,db:db_dependency, current_data: Tuple[User,WeaviateData]  = Depends(get_current_user)):
    try:
        data=await request.json()
        query= data['query']
        print(current_data)
        className=current_data[1].className
        if "price" in data:
            search_result=weaviate_filter_price(data,className,query)
        else:
            search_result=weaviate_middleware_search(request,db,current_data,query)    
    except Exception as e:
        raise Exception(e)
    return search_result