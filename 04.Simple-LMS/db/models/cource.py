from datatime import datetime
import enum

from sqlalchemy import Enum , Column , ForeignKey , Integer , String , String , Text , Boolean
from sqlalchemy.orm import relationships
from sqlalchemy_utils import URLType
from ..db_setup import Timestamps,Base
from .user import User
from .mixins import Timestamp

class ContentType(enum.Enum):
    lesson=1
    quiz=2
    assignment=3
    
class Cource(Timestamp,Timestamps,Base):
    __tablename__="cources"
    id=Column(Integer , primary_key=True , index=True)
    title=Column(String(200),nullable=False)
    description=Column(Text,nullable=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    created_by=relationship(User)
    cource=relationship("course",back_populates="sections")
    content_blocks=relatinship("ContentBlock",back_populates="Section")
    
class Section(Timestamps,Base):
    __tablename__="content_blocks"
    id=Column(Integer , primary_key=True , index=True)
    title=Column(String(200),nullable=False)
    description=Column(Text,nullable=True)
    url=Column(URLType,nullable=True)
    cource_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    cource=relationship("cource",back_populated="sections")
    content_blocks=relatinship("ContentBlock",back_populates="Section")
   

class ContentBlock(Timestamps,Base):
    __tablename__="content_blocks"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(200),nullable=False)
    description=Column(Text,nullable=True)
    content=Column(Text , nullable=True)
    section_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    section=relationship("Section",back_populates="content_blocks")
    completed_content_blocks=relationship("CompletedContentBlock",back_populates="content_blocks")
    
class StudentCource(Timestamps,Base):
    __tablename__="student cources"
    id=Column(Integer,primary_key=True,index=True)
    student_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    cource_id=Column(Integer,ForeignKey("courses.id"),nullable=False)
    completed=Column(Boolean,default=False)
    student=relationship("User",back_populates="student_courses")
    cource=relationship("Cource",back_populates="student_courses")
    
    
class CompletedContentBlock(Timestamps,Base):
    __tablename__="completed content block"
    id=Column(Integer,primary_key=True,index=True)
    student_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    content_block_id=Column(Integer,ForeignKey("content_blocks.id"),nullable=False)
    url=Column(URLType,nullable=True)
    feedback=Column(Text,nullable=True)
    grade=Column(Integer,default=0)
    student=relationship("User",back_populates="student_content_blocks")
    content_block=relationship(ContentBlock,back_populates="completed_content_blocks")