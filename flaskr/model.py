import datetime
import sqlalchemy
from flaskr.database import Base
from sqlalchemy import Column, Integer, Text , DateTime
from flaskr import app


class Entry(base):
  __tablename__ = "entries"
  id = Column(Integer,Sequence('entries_id_seq'),primary_key=True)
  title = Column(Text)
  content = Column(Text)
  created_at =Column(DateTime)
  updated_at =Column(DateTime)