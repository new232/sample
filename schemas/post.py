# schemas/post.py
from pydantic import BaseModel, ConfigDict  # BaseModel: Pydantic 모델 정의용, ConfigDict: 설정 지정용
from typing import Optional

# 📌 지도 조회 (전체 or 태그 기반) 시 사용하는 응답 모델
class PostMapOut(BaseModel):
    id: int             # 게시물 고유 ID
    latitude: float     # 위도
    longitude: float    # 경도
    tag: str            # 태그 (예: '치즈냥')

    # 🔧 Pydantic v2에서는 from_attributes=True로 ORM 연동 설정
    model_config = ConfigDict(from_attributes=True)

# 📌 단일 게시물 조회 시 사용하는 응답 모델
class PostOut(BaseModel):
    id: int             # 게시물 고유 ID
    title: str          # 제목
    latitude: float     # 위도
    longitude: float    # 경도
    tag: str            # 태그

    model_config = ConfigDict(from_attributes=True)
