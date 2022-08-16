import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class follower(Base):
    __tablename__ ='follower'
    follower_id = Column(Integer, primary_key=True)
    fk_user_from_id = Column(Integer,ForeignKey('user.user_id'))
    fk_user_to_id = Column(Integer,ForeignKey('user.user_id'))

class user(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_firstname = Column(String(50), nullable=False)
    user_lastname = Column(String(50), nullable=False)
    user_email = Column(String(10), nullable=False)

    follower = relationship('follower',backref='user',lazy=True)
    comment = relationship('comment',backref='user',lazy=True)
    post = relationship('post',backref='user',lazy=True)

class media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    media_type = Column(String(50), nullable=False)
    fk_post_id = Column(Integer,ForeignKey('post.post_id'))

    media_url = relationship('favoritos',backref='personajes',lazy=True)
    

class comment(Base):
    __tablename__ = 'comment'
    comment_id =  Column(Integer, primary_key=True)
    comment_text = Column(String(200), nullable=False)
    fk_author_id = Column(Integer,ForeignKey('user.user_id'))
    fk_post_id = Column(Integer,ForeignKey('post.post_id'))

class post(Base):
    __tablename__ = 'post'
    post_id =  Column(Integer, primary_key=True)
    fk_user_id = Column(Integer,ForeignKey('user.user_id'))
    fk_planetas = Column(Integer,ForeignKey('planetas.id_planetas'))
    fk_personajes = Column(Integer,ForeignKey('personajes.id_personajes'))
    
    comment = relationship('comment',backref='post',lazy=True)
    media = relationship('media',backref='post',lazy=True)
    
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')