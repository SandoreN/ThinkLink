from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db
import datetime

class User(db.Model):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    is_confirmed = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    registration_date = Column(DateTime, default=datetime.datetime.now())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'is_confirmed': self.is_confirmed,
            'is_admin': self.is_admin,
            'registration_date': self.registration_date.strftime('%Y-%m-%d %H:%M:%S')
        }


class Team(db.Model):
    __tablename__ = 'Team'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    creator_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    creator = relationship('User', backref='teams')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'creator_id': self.creator_id
        }


class Message(db.Model):
    __tablename__ = 'Message'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    subject = Column(String(100))
    text = Column(Text, nullable=False)
    sent_date = Column(DateTime, default=datetime.datetime.now())

    def serialize(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'recipient_id': self.recipient_id,
            'subject': self.subject,
            'text': self.text,
            'sent_date': self.sent_date.strftime('%Y-%m-%d %H:%M:%S')
        }

class Project(db.Model):
    __tablename__ = 'Project'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    resource_id = Column(Integer, ForeignKey('Resource.id'), nullable=False)
    team_id = Column(Integer, ForeignKey('Team.id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    is_published = Column(Boolean, default=False)
    is_proposal = Column(Boolean, default=False)
    team = relationship('Team', backref='projects')
    creator = relationship('User', backref='created_projects')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'resource_id': self.resource_id,
            'team_id': self.team_id,
            'creator_id': self.creator_id,
            'is_published': self.is_published,
            'is_proposal': self.is_proposal
        }


class Draft(db.Model):
    __tablename__ = 'Draft'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    project_id = Column(Integer, ForeignKey('Project.id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    upload_date = Column(DateTime, default=datetime.datetime.now())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'content': self.content,
            'project_id': self.project_id,
            'creator_id': self.creator_id,
            'upload_date': self.upload_date.strftime('%Y-%m-%d %H:%M:%S')
        }


class Resource(db.Model):
    __tablename__ = 'Resource'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    file_path = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False)
    project_id = Column(Integer, ForeignKey('Project.id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'file_path': self.file_path,
            'type': self.type,
            'project_id': self.project_id,
            'creator_id': self.creator_id
        }

class Task(db.Model):
    __tablename__ = 'Task'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    project_id = Column(Integer, ForeignKey('Project.id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    due_date = Column(DateTime)
    is_completed = Column(Boolean, default=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'project_id': self.project_id,
            'creator_id': self.creator_id,
            'due_date': self.due_date.strftime('%Y-%m-%d %H:%M:%S') if self.due_date else None,
            'is_completed': self.is_completed
        }


class Proposal(db.Model):
    __tablename__ = 'Proposal'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    resource_ID = Column(Integer, ForeignKey('Resource.resource_id'), nullable=False)
    project_ID = Column(Integer, ForeignKey('Project.project_id'), nullable=False)
    authors = relationship('Author', secondary='proposal_author')

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'resource_ID': self.resource_ID,
            'project_ID': self.project_ID,
            'authors': [author.serialize() for author in self.authors]
        }


class Publication(db.Model):
    __tablename__ = 'Publication'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    resource_ID = Column(Integer, ForeignKey('Resource.resource_id'), nullable=False)
    project_ID = Column(Integer, ForeignKey('Project.project_id'), nullable=False)
    authors = relationship('Author', secondary='publication_author')

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'resource_ID': self.resource_ID,
            'project_ID': self.project_ID,
            'authors': [author.serialize() for author in self.authors]
        }
    
class Author(db.Model):
    __tablename__ = 'Author'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    affiliation = Column(String(100))
    email = Column(String(100))
    location = Column(String(100))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'affiliation': self.affiliation,
            'email': self.email,
            'location': self.location
        }