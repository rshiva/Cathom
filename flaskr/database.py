import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String , Text , Boolean , DateTime, MetaData, Table ,Sequence,ForeignKey 

#Base = declarative_base()
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://admin:desidime123@localhost:5432/test_table'
db = SQLAlchemy(app)
metadata = MetaData()


entries = Table('entries', metadata,
    Column('id', Integer, Sequence('entries_id_seq') ,primary_key = True),
    Column('title', Text),
    Column('content', Text),
    Column('photo_name',String),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
    extend_existing=True
    )

db.create_all()