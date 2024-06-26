from middleware.weaviate import weaviate_middleware_add_data, weaviate_create_schema
from fastapi import Depends, APIRouter, Request,File, UploadFile
from middleware.pasql_mid import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated,List,Tuple
from models.user import User , WeaviateData 
from middleware.jwt_auth import get_current_user
from fastapi import HTTPException
from middleware.weavaite_image import weaviate_image_middleware_add_data, weaviate_image_create_schema

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/setup",
    tags=["setups"],
    responses={404: {"description": "Not found"}}
)

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/schema", response_model=str)
async def weaviate_set_up_schema(request:Request,db: db_dependency,current_data: Tuple[User,WeaviateData]  = Depends(get_current_user)):
    try:
        data = await request.json()
        className=current_data[1].className
        properties=data['properties']        
        creation_result = weaviate_create_schema(className, properties=properties)
        return creation_result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/add_data", response_model=str)
def weaviate_add_data(request:Request,db: db_dependency,current_user: User = Depends(get_current_user),file:UploadFile = File(...)):
    try:
        add_result = weaviate_middleware_add_data(request, current_user,db,file)
        return add_result
    except Exception as e:
        raise Exception(e)
    

# Images with weaviate

@router.post("/schema_with_image", response_model=str)
async def weaviate_set_up_schema(request:Request,db: db_dependency,current_data: Tuple[User,WeaviateData]  = Depends(get_current_user)):
    try:
        data = await request.json()
        className=current_data[1].className
        properties=data['properties']        
        creation_result = weaviate_image_create_schema(className, properties=properties)
        return creation_result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/add_data_with_image", response_model=str)
def weaviate_add_data(request:Request,db: db_dependency,current_user: User = Depends(get_current_user),file:UploadFile = File(...)):
    try:
        add_result = weaviate_image_middleware_add_data(request, current_user,db,file)
        return add_result
    except Exception as e:
        raise Exception(e)    