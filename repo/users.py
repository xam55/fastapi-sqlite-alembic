from sqlalchemy.ext.asyncio import AsyncSession
from core.models.users import User
from sqlalchemy import select


class UserRepo:

    def __init__(self,session: AsyncSession):
        self.session = session


    async def user_create(self,email:str,name:str,password:str):
        user=User(email=email,name=name,password=password)

        self.session.add(user)
        await self.session.flush()
        return user
    

    async def get_users(self)->list[User]:
        result=await self.session.execute(select(User))
        return list(result.scalars().all())
    
    async def get_user_by_id(self,user_id:int)->User | None:
        result=await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    

    async def update_email(self,user_id:int,new_email:str):
        user=await self.get_user_by_id(user_id=user_id)
        if user is None:
            return None
        
        user.email = new_email

        await self.session.flush()
        return user
    

    async def update_password(self,user_id:int,new_password:str):
        user = await self.get_user_by_id(user_id)
        if user is None:
            return None
        
        user.password = new_password
        await self.session.flush()
        return user

    async def update_name(self,user_id:int,new_name:str):
        user= await self.get_user_by_id(user_id=user_id)
        if user is None:
            return None
        
        user.name= new_name
        await self.session.flush()
        return user 
    
    async def delete_user(self,user_id:int)-> True | None:
        user= await self.get_user_by_id(user_id=user_id)
        if user is None:
            return None
        
        await self.session.delete(user)
        await self.session.flush()
        return True
        
        

    

    


