from sqlalchemy import Column, Integer, String, Text, JSON
from db import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    title = Column(String)
    summary = Column(Text)
    sections = Column(JSON)
    quiz = Column(JSON)
    related_topics = Column(JSON)
