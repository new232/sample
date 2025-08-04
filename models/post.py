from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    tag: Mapped[str] = mapped_column(String)
