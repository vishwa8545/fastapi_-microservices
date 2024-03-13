from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table
from sqlalchemy.orm import relationship

from .database import Base
user_project_association = Table(
    'user_project',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('project_id', Integer, ForeignKey('projects.id'))
)
class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    projects = relationship('Project', secondary=user_project_association, back_populates='projects')

class Project(Base):
    __tablename__='projects'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, unique=True)
    users = relationship('User', secondary=user_project_association, back_populates='users')

