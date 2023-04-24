from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///naver_api.db', echo=True)

Base = declarative_base()


class WebtoonRank(Base):
    __tablename__ = 'webtoon_rank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rank = Column(Integer)
    star = Column(Float)
    title = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, rank, star, title):
        self.rank = rank
        self.star = star
        self.title = title
    def __repr__(self):
        return f"WebtoonRank(id={self.id!r}, rank={self.rank!r}, star={self.star!r}, title={self.title!r}, created_at={self.created_at!r})"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

rank = 1
title = '짱구는 못말려'
star = 9.8
new_rank = WebtoonRank(rank, star, title)
session.add(new_rank)
session.commit()

print(new_rank)
