from fastapi import FastAPI, Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.config import settings

def init_dependencies(app: FastAPI):
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    app.state.db = SessionLocal


def get_db(request: Request):
    db = request.app.state.db()
    try:
        yield db
    finally:
        if db:
            db.close()