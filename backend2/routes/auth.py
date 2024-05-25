from datetime import timedelta
from fastapi import Depends, APIRouter, Request, Form
from middleware.jwt_auth import authenticate_user, create_access_token, get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.auth_model import Token, UserBase,UserCreate
from middleware.pasql_mid import SessionLocal, engine, Base
from models.user import User, WeaviateData
from sqlalchemy.orm import Session
from typing import Annotated, Optional
from jose import JWTError,jwt
from passlib.context import CryptContext
import random
import string


router = APIRouter(
    prefix="/auth",
    tags=["authentications"],
    responses={404: {"description": "Not found"}}
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_random_string(length: int) -> str:
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    random_string="Class_"+random_string
    return random_string

db_dependency = Annotated[Session, Depends(get_db)]


async def get_current_user(db: db_dependency,token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user


@router.post("/token", response_model=Token)
async def login_for_access_token(db: db_dependency,form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.username, form_data.password)
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        db_weaviate = db.query(WeaviateData).filter(WeaviateData.user_id == user.id).first()
        if not db_weaviate:
            random_string = generate_random_string(10)
            db_weaviate = WeaviateData(className=random_string,user_id=user.id)
            db.add(db_weaviate)
            db.commit()
            db.refresh(db_weaviate)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    className= random_string if not db_weaviate else db_weaviate.className
    access_token = create_access_token(
        data={"sub": user.username,"className":className}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/users/create", response_model=UserBase)
def create_user(db: db_dependency,user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/me")
async def read_users_me(current_data: tuple[User , WeaviateData]= Depends(get_current_user)):
    return current_data[0]

