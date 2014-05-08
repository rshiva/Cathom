import datetime
import sqlalchemy
from flaskr.database import db
from sqlalchemy import Column, Integer, Text , DateTime
from flaskr import app
from sqlalchemy import Sequence



class Entry(db.Model):
  __tablename__ = "entries"
  id = db.Column(db.Integer,Sequence('entries_id_seq'),primary_key=True)
  title = db.Column(db.Text)
  content = db.Column(db.Text)
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)


  def __init__(self,title,content):
    self.title = title
    self.content = content
    self.created_at=datetime.datetime.utcnow()
    self.updated_at=datetime.datetime.utcnow()

  def __repr__(self):
    return '<Title %r>' % self.title 