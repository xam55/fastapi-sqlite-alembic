from datetime import datetime

from sqlalchemy import String,func
from sqlalchemy.orm import mapped_column,Mapped,relationship

from core.database import Base

class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(
        primary_key=True,
        unique=True
    )
    name : Mapped[str] = mapped_column(String(50))
    email : Mapped[str] = mapped_column(String(50),unique=True,index=True)
    is_active: Mapped[bool] = mapped_column(default=True)

    create_at: Mapped[datetime] = mapped_column(server_default=func.now)
    uppdate_at: Mapped[datetime] = mapped_column(server_default=func.now)
    
    def __repr__(self)-> str:
        return f"<User id={self.id} email={self.email!r} >"
    