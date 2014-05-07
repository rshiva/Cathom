import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
             render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String , Text , Boolean , DateTime, MetaData, Table ,Sequence,ForeignKey 


app=Flask(__name__)
db_name="postgresql+psycopg2://admin:desidime123@localhost:5432/test_table"
engine = create_engine(db_name,echo=True) 
Session = sessionmaker(autocommit=False ,bind=engine)
connection = engine.connect()
metadata = MetaData()


entries = Table('entries', metadata,
    Column('id', Integer, Sequence('entries_id_seq') ,primary_key = True),
    Column('title', Text),
    Column('content', Text),
    extend_existing=True
    )

metadata.create_all(engine) 