from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base
from datetime import datetime


Base = declarative_base()

class WebtoonRank(Base):
    __tablename__ = 'webtoon_rank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    day = Column(String)
    rank = Column(Integer)
    star = Column(Float)
    title = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, day, rank, star, title):
        self.day = day
        self.rank = rank
        self.star = star
        self.title = title
    def __repr__(self):
        return f"WebtoonRank(id={self.id!r}, day={self.day!r} rank={self.rank!r}, star={self.star!r}, title={self.title!r}, created_at={self.created_at!r})"