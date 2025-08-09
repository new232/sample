from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)  # ✅ 자동 증가
    title: Mapped[str] = mapped_column(String)  # 제목
    latitude: Mapped[float] = mapped_column(Float)  # 위도
    longitude: Mapped[float] = mapped_column(Float)  # 경도
    tag: Mapped[str] = mapped_column(String)  # 태그 (예: 치즈냥, 길냥이 등)
    image_url: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    likes: Mapped[int] = mapped_column(Integer, default=0)