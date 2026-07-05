from core.models.users import User
from repo.users import UserRepo

class UserServise:
    def __init__(self,repo: UserRepo):
        self.repo=repo

    async def create_user(self,name:str,email:str)->User:
        if not isinstance(name,str) or not name.strip():
            raise TypeError("user is not str")
        if not isinstance(email,str) or not email.strip():
            raise TypeError("email is  not str")
        
        user=await self.repo.user_create(
            email=email,
            name=name)

        await self.repo.session.commit()
        return user
    
    async def get_users(self)-> list[User]:
        user=await self.repo.get_users()
        return user
    
    async def get_user_by_id(self,user_id:int) -> User | None:
        if not isinstance(user_id,int):
            raise TypeError("user_id is not int")
        
        user = await self.repo.get_user_by_id(user_id=user_id)
        await self.repo.session.commit()
        return user
    
    async def update_email(self,user_id:int,new_email:str)-> User | None:
        if not isinstance(user_id,int):
            raise TypeError("user_id is not int")
        
        if not isinstance(new_email,str) or not new_email.strip():
            raise TypeError("email is not str")
        
        user = await self.repo.update_email(user_id=user_id,new_email=new_email)
        
        await self.repo.session.commit()
        return user
    
    async def update_name(self,user_id: int, new_name:str)->User | None:
        user= await self.repo.get_user_by_id(user_id=user_id)

        if user is None:
            return None
        
        user.name = new_name
        await self.repo.session.commit()
        return user
    
    async def delete_user(self,user_id:int)->True | None:
        user=await self.repo.get_user_by_id(user_id=user_id)
        if user is None:
            return None
        
        await self.repo.delete_user(user_id=user_id)
        await self.repo.session.commit()
        return True
    




 
    































