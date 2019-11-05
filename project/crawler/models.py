from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
session = sessionmaker(engine)()

Base = declarative_base()

class LinksQueueItem(Base):
    __tablename__ = 'links_queue'
    id = Column(Integer, primary_key=True)
    link = Column(String, index=True)


class CrawlerItem(Base):
    __tablename__ = 'crawler_items'
    id = Column(Integer, primary_key=True)
    link = Column(String)
    response = Column(Integer)
    title = Column(String)
    description = Column(String)
    h1 = Column(String)


Base.metadata.create_all(engine)
