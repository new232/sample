from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.post import Post
from schemas.post import PostMapOut, PostOut
from typing import List

router = APIRouter()


# 🧩 DB 세션 연결 함수 (의존성 주입용)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 📍 전체 지도용 API (위도/경도가 존재하는 모든 게시글 반환)
@router.get("/posts/map", response_model=List[PostMapOut])
def get_map_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return [post for post in posts if post.latitude is not None and post.longitude is not None]


# 🐱 태그 필터 기반 지도 조회 API
@router.get("/posts/by-tag", response_model=List[PostMapOut])
def get_posts_by_tag(tag: str = Query(...), db: Session = Depends(get_db)):
    posts = (
        db.query(Post)
        .filter(Post.tag == tag)
        .filter(Post.latitude.isnot(None), Post.longitude.isnot(None))
        .all()
    )
    return posts


# 🔎 단일 게시글 상세 조회 (ID 기반)
@router.get("/posts/{post_id}", response_model=PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")  # 없는 ID 처리
    return post
