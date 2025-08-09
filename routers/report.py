from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.post import Post

router = APIRouter()

# DB 세션
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ 게시글 신고 API
@router.post("/posts/{post_id}/report")
def report_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="해당 게시글을 찾을 수 없습니다.")
    return {"message": "신고가 접수되었습니다."}