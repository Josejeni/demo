from numbers import Integral
from .database import Base
from sqlalchemy import Column,String,Integer,ForeignKey

class log(Base):
    __tablename__="JWTsam"
    user_name=Column(String,primary_key=True)
    password=Column(String)
    title=Column(String)
    content=Column(String)

class users(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    username=Column(String,nullable=False)
    password=Column(String,nullable=False)
    phone_no=Column(String)

class posts(Base):
    __tablename__="post"
    id=Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    title=Column(String)
    content=Column(String)

class Vote(Base):
    __tablename__="Votes"
    post_id=Column(Integer,ForeignKey("post.id",ondelete="CASCADE"),primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    
class sam(Base):
    __tablename__="mercy"
    id=Column(Integer,primary_key=True,nullable=True)
    title=Column(Integer)