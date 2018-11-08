import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import desc
from sqlalchemy import create_engine

Base = declarative_base()
# days
class Day(Base):
    __tablename__ = 'day'

    id = Column(Integer, primary_key=True)
    date = Column(String(250), nullable=False)
    href = Column(String(250), nullable=False)
    text = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'href': self.href,
            'text': self.text
        }
engine = create_engine('sqlite:///days.db')
Base.metadata.create_all(engine)
