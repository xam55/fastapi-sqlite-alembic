# routers/__init__.py

from fastapi import APIRouter

from .users import router as users

router = APIRouter(prefix="/api")

router.include_router(users)