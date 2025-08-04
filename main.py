from fastapi import FastAPI
from database import Base, engine
from routers import post,report

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router, prefix="/api")
app.include_router(report.router, prefix="/api")
