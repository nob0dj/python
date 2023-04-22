from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///example.db', echo=True)

Base = declarative_base()


class WebtoonsRank(Base):
    __tablename__ = 'webtoons_rank'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rank = Column(Integer)
    title = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, rank, title):
        self.rank = rank
        self.title = title
        self.created_at = Column(DateTime, default=datetime.now())


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

rank = 1
title = '짱구는 못말려'
new_rank = WebtoonsRank(rank, title)
session.add(new_rank)
session.commit()
