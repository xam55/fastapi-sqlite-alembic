from fastapi import APIRouter,Depends,HTTPException
from starlette import status
from core.deps import get_user_servise
from schemas.users import (
    UserCreate,
    UserEmail,
    UserName,
    UserRead,)

from services.users import UserServise

router= APIRouter(prefix="/users",tags=["users"])


@router.get("/",status_code=status.HTTP_200_OK)
async def get_users(service: UserServise = Depends(get_user_servise))->list[UserRead]:
    users=await service.get_users()
    return users

@router.get("/{user_id}",status_code=status.HTTP_200_OK)
async def get_user(user_id:int,service: UserServise = Depends(get_user_servise)):
    user=await service.get_user_by_id(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="user not found")
    
    return user


@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user(name:str,email:str,service: UserServise = Depends(get_user_servise)):

    user=await service.create_user(name=name,email=email)
    return user

@router.patch("/{user_id}/email")
async def update_email(user_id:int,new_email:str,service: UserServise = Depends(get_user_servise)):
    user=await service.update_email(user_id=user_id,new_email=new_email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    return user

@router.patch("/{user_id}/name")
async def update_name(user_id:int,new_name:str,service: UserServise = Depends(get_user_servise)):
    user=await service.update_name(user_id=user_id,new_name=new_name)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    
    return user

@router.delete("/{user_id}")
async def delete_user(user_id:int, service: UserServise = Depends(get_user_servise)):
    user = await service.delete_user(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    
    return {"status":"ok"}
