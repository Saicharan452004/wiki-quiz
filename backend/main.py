from dotenv import load_dotenv
load_dotenv()
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from fastapi import Depends
from scraper import scrape_wikipedia
from quiz_generator import generate_quiz
from models import Quiz
from fastapi import FastAPI
from fastapi import Query
from db import engine
from models import Base
from sqlalchemy.orm import Session
from db import SessionLocal


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate")
def generate_quiz_api(url: str = Query(...),db: Session = Depends(get_db)):
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    # 1. Check if URL already exists
    existing = db.query(Quiz).filter(Quiz.url == url).first()

    if existing:
        return {
            "id": existing.id,
            "url": existing.url,
            "title": existing.title,
            "summary": existing.summary,
            "sections": existing.sections,
            "quiz": existing.quiz,
            "related_topics": existing.related_topics
        }

    # 2. If not cached, generate new
    data = scrape_wikipedia(url)
    quiz_data = generate_quiz(data["text"])

    record = Quiz(
        url=url,
        title=data["title"],
        summary=data["summary"],
        sections=data["sections"],
        quiz=quiz_data["quiz"],
        related_topics=quiz_data["related_topics"]
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "id": record.id,
        "url": url,
        "title": data["title"],
        "summary": data["summary"],
        "sections": data["sections"],
        "quiz": quiz_data["quiz"],
        "related_topics": quiz_data["related_topics"]
    }


@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    records = db.query(Quiz).all()

    return [
        {
            "id": r.id,
            "url": r.url,
            "title": r.title
        }
        for r in records
    ]

@app.get("/quiz/{quiz_id}")
def get_quiz_details(quiz_id: int, db: Session = Depends(get_db)):
    record = db.query(Quiz).filter(Quiz.id == quiz_id).first()

    if not record:
        return {"error": "Quiz not found"}

    return {
        "id": record.id,
        "url": record.url,
        "title": record.title,
        "summary": record.summary,
        "sections": record.sections,
        "quiz": record.quiz,
        "related_topics": record.related_topics
    }

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"status": "ok"}
