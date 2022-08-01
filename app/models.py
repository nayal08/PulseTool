from ast import Str
import email
from email.policy import default
from enum import unique
from operator import index
import string
from sqlalchemy import Column, ForeignKey, Integer, String,Enum
from database import Base


class Account(Base):
    __tablename__ ="account"

    id = Column(Integer, primary_key=True)
    account_id=Column(String,unique=True,index=True,nullable=False)
    full_name=Column(String,default=None)
    email=Column(String,default=None,unique=True,index=True)
    upvote=Column(Integer,unique=True, index=True,default=0)
    downvote=Column(Integer,unique=True, index=True,default=0)
    account_type = Column(Enum('Founder', 'Investor', 'Whale', 'Influencer',name='Profile_types'))
    rating=Column(Integer,unique=True, index=True,default=0)
    youtubelink=Column(string,default=None)
    bio=Column(String,default=None)

class SocialMedia(Base):
    __tablename__="socialmedia"

    id = Column(Integer, primary_key=True, index=True)
    user_id=Column(String,ForeignKey(Account.id))
    website=Column(String, default=None)
    telegram=Column(String, default=None)
    twitter=Column(String, default=None)
    github=Column(String, default=None)
    unicrypt=Column(String,default=None)
    

class Reaction(Base):
    __tablename__="reaction"

    id = Column(Integer, primary_key=True)
    user_id=Column(String,ForeignKey(Account.id))
    super_duper=Column(Integer,unique=True, index=True,default=0)
    smiley=Column(Integer,unique=True, index=True,default=0)
    heart=Column(Integer,unique=True, index=True,default=0)
    dislike=Column(Integer,unique=True, index=True,default=0)

class UserAchievements(Base):
    __tablename__="userachievements"
    id = Column(Integer, primary_key=True)
    user_id=Column(String,ForeignKey(Account.id))
    founder=Column(String, default=None)
    investor=Column(String, default=None)
    whale=Column(String, default=None)
    influencer=Column(String, default=None)










