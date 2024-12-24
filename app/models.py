from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Term(Base):
    __tablename__ = 'terms'

    id = Column(Integer, primary_key=True, index=True)
    term = Column(String, index=True, unique=True)
    description = Column(String)
