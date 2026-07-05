from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.database import get_db
from services.users import UserServise
from repo.users import UserRepo

DB=DEPS=Annotated[AsyncSession,Depends(get_db)]



def get_user_servise(session: AsyncSession = Depends(get_db))->UserServise:
    return UserServise(UserRepo(session=session))
