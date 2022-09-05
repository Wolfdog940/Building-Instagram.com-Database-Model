import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False , unique=True)
    firstname = Column(String(250), nullable=False , unique=True)
    lastname = Column(String(250), nullable=False , unique=True)
    email = Column(String(250), nullable=False , unique=True)
    

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id =  Column(Integer, ForeignKey('user.id'))


class Media(Base):
    __tablename__ = 'media'
   
    id = Column(Integer, primary_key=True)
    type = Column(Enum , nullable=False , unique=True,)
    url =Column(String(250), nullable=False , unique=True)
    post_id =Column(Integer, ForeignKey('post.id'),nullable=False , unique=True)


class Post(Base):
    __tablename__ = 'post'
   
    id = Column(Integer, primary_key=True)
    user_id =Column(Integer, ForeignKey('user.id'))


class Comment(Base):
    __tablename__ = 'Comment'
   
    id = Column(Integer, primary_key=True)
    coment_text = Column(String(250), nullable=False , unique=True)
    author_id =Column(Integer, ForeignKey('user.id'),nullable=False , unique=True)
    post_id =Column(Integer, ForeignKey('post.id'),nullable=False , unique=True)
   
   
   
   
  


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e