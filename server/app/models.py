from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db
import time

class User(db.Model):
    __tablename__ = 'User'

    UserID = Column(Integer, primary_key=True)
    Username = Column(String(50), nullable=False, unique=True)
    Email = Column(String(100), nullable=False, unique=True)
    PasswordHash = Column(String(255), nullable=False)
    IsConfirmed = Column(Boolean, default=False)
    IsAdmin = Column(Boolean, default=False)
    RegistrationDate = Column(DateTime, default=time.time())

class Team(db.Model):
    __tablename__ = 'Team'

    TeamID = Column(Integer, primary_key=True)
    TeamName = Column(String(100), nullable=False)
    Description = Column(Text)
    CreatorID = Column(Integer, ForeignKey('User.UserID'), nullable=False)
    creator = relationship('User', backref='teams')

class Message(db.Model):
    __tablename__ = 'Message'

    MessageID = Column(Integer, primary_key=True)
    SenderID = Column(Integer, ForeignKey('User.UserID'), nullable=False)
    RecipientID = Column(Integer, ForeignKey('User.UserID'), nullable=False)
    Subject = Column(String(100))
    MessageText = Column(Text, nullable=False)
    SentDate = Column(DateTime, default=time.time())

class Project(db.Model):
    __tablename__ = 'Project'

    ProjectID = Column(Integer, primary_key=True)
    ProjectName = Column(String(100), nullable=False)
    Description = Column(Text)
    ResourceDir = Column(String(255), nullable=False)
    TeamID = Column(Integer, ForeignKey('Team.TeamID'), nullable=False)
    CreatorID = Column(Integer, ForeignKey('User.UserID'), nullable=False)
    IsPrivate = Column(Boolean, default=False)
    team = relationship('Team', backref='projects')
    creator = relationship('User', backref='created_projects')

class Draft(db.Model):
    __tablename__ = 'Draft'

    DraftID = Column(Integer, primary_key=True)
    DraftName = Column(String(100), nullable=False)
    Content = Column(Text, nullable=False)
    ProjectID = Column(Integer, ForeignKey('Project.ProjectID'), nullable=False)
    CreatorID = Column(Integer, ForeignKey('User.UserID'), nullable=False)
    UploadDate = Column(DateTime, default=time.time())

class Resource(db.Model):
    __tablename__ = 'Resource'

    ResourceID = Column(Integer, primary_key=True)
    ResourceName = Column(String(100), nullable=False)
    FilePath = Column(String(255), nullable=False)
    ResourceType = Column(String(50), nullable=False)
    ProjectID = Column(Integer, ForeignKey('Project.ProjectID'), nullable=False)
    CreatorID = Column(Integer, ForeignKey('User.UserID'), nullable=False)

class Task(db.Model):
    __tablename__ = 'Task'

    TaskID = Column(Integer, primary_key=True)
    TaskName = Column(String(100), nullable=False)
    Description = Column(Text)
    ProjectID = Column(Integer, ForeignKey('Project.ProjectID'), nullable=False)
    CreatorID = Column(Integer, ForeignKey('User.UserID'), nullable=False)
    DueDate = Column(DateTime)
    IsCompleted = Column(Boolean, default=False)

class Proposal(db.Model):
    __tablename__ = 'Proposal'

    ProposalID = Column(Integer, primary_key=True)
    ProposalTitle = Column(String(100), nullable=False)
    FilePath = Column(String(255), nullable=False)
    CreatorID = Column(Integer, ForeignKey('User.UserID'), nullable=False)
    SubmissionDate = Column(DateTime, default=time.time())
    Flags = Column(Integer, nullable=False, default=0)

class Publication(db.Model):
    __tablename__ = 'Publication'

    PublicationID = Column(Integer, primary_key=True)
    PublicationName = Column(String(100), nullable=False)
    FilePath = Column(String(255), nullable=False)
    ProjectID = Column(Integer, ForeignKey('Project.ProjectID'), nullable=False)
    CreatorID = Column(Integer, ForeignKey('User.UserID'), nullable=False)
    PublicationDate = Column(DateTime, default=time.time())
    Flags = Column(Integer, nullable=False, default=0)

