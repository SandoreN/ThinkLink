from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db
import datetime

team_members = db.Table('team_members',
    db.Column('user_id', db.Integer, db.ForeignKey('User.id'), primary_key=True),
    db.Column('team_id', db.Integer, db.ForeignKey('Team.id'), primary_key=True)
)

project_members = db.Table('project_members',
    db.Column('user_id', db.Integer, db.ForeignKey('User.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('Project.id'), primary_key=True)
)

teams = relationship('Team', secondary=team_members, backref='users')
projects = relationship('Project', secondary=project_members, backref='users')

class User(db.Model):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    is_confirmed = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    registration_date = Column(DateTime, default=datetime.datetime.now)
    teams = relationship('Team', secondary=team_members, backref='users')

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
    projects = relationship('Project', backref='team')
    creation_date = Column(DateTime, default=datetime.datetime.now)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'creator_id': self.creator_id,
            'creation_date': self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        }


class Message(db.Model):
    __tablename__ = 'Message'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    subject = Column(String(100))
    text = Column(Text, nullable=False)
    sent_date = Column(DateTime, default=datetime.datetime.now)
    parent_id = Column(Integer, ForeignKey('Message.id'))

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
    resource_dir = Column(String, nullable=False)
    is_published = Column(Boolean, default=False)
    is_proposal = Column(Boolean, default=False)
    team_id = Column(Integer, ForeignKey('Team.id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    creator = relationship('User', backref='projects')
    drafts = relationship('Draft', backref='project', lazy=True)
    resources = relationship('Resource', backref='project', lazy=True)
    tasks = relationship('Task', backref='project', lazy=True)
    creation_date = Column(DateTime, default=datetime.datetime.now)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'resource_dir': self.resource_dir,
            'is_published': self.is_published,
            'is_proposal': self.is_proposal,
            'team_id': self.team_id,
            'creator_id': self.creator_id,
            'creation_date': self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        }


class Draft(db.Model):
    __tablename__ = 'Draft'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    project_id = Column(Integer, ForeignKey('Project.id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    creation_date = Column(DateTime, default=datetime.datetime.now)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'content': self.content,
            'project_id': self.project_id,
            'creator_id': self.creator_id,
            'creation_date': self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        }


class Resource(db.Model):
    __tablename__ = 'Resource'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    file_path = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False)
    project_id = Column(Integer, ForeignKey('Project.id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    upload_date = Column(DateTime, default=datetime.datetime.now)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'file_path': self.file_path,
            'type': self.type,
            'project_id': self.project_id,
            'creator_id': self.creator_id,
            'upload_date': self.upload_date.strftime('%Y-%m-%d %H:%M:%S')
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
    creation_date = Column(DateTime, default=datetime.datetime.now)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'project_id': self.project_id,
            'creator_id': self.creator_id,
            'due_date': self.due_date.strftime('%Y-%m-%d %H:%M:%S') if self.due_date else None,
            'is_completed': self.is_completed,
            'creation_date': self.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        }


class Proposal(db.Model):
    __tablename__ = 'Proposal'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    category = Column(String(50))
    resource_id = Column(Integer, ForeignKey('Resource.id'), nullable=False)
    project_id = Column(Integer, ForeignKey('Project.id'), nullable=False)
    project = relationship('Project', backref='proposal', uselist=False)
    team_id = Column(Integer, ForeignKey('Team.id'), nullable=False)  # Add foreign key constraint
    team = relationship('Team', backref='proposals')
    proposal_date = Column(DateTime, default=datetime.datetime.now)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'resource_id': self.resource_id,
            'project': self.project_id,
            'team': self.team_id,
            'proposal_date': self.proposal.strftime('%Y-%m-%d %H:%M:%S')
        }

class Publication(db.Model):
    __tablename__ = 'Publication'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    category = Column(String(50))
    resource_id = Column(Integer, ForeignKey('Resource.id'), nullable=False)
    project_id = Column(Integer, ForeignKey('Project.id'), nullable=False)
    team_id = Column(Integer, ForeignKey('Team.id'), nullable=False)
    project = relationship('Project', backref='publication', uselist=False)
    team = relationship('Team', backref='publication')
    publication_date = Column(DateTime, default=datetime.datetime.now)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'resource_id': self.resource_id,
            'project_id': self.project_id,
            'team_id': self.team_id,
            'publication_date': self.publication_date.strftime('%Y-%m-%d %H:%M:%S')
        }

class Token(db.Model):
    __tablename__ = 'Token'

    id = Column(Integer, primary_key=True)
    token = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    is_blacklisted = Column(Boolean, default=False)
    creation_date = Column(DateTime, default=datetime.datetime.now)
    expiration_date = Column(DateTime)

    def serialize(self):
        return {
            'id': self.id,
            'token': self.token,
            'is_blacklisted': self.blacklisted,
            'creation_date': self.creation_date.strftime('%Y-%m-%d %H:%M:%S'),
            'expiration_date': self.expiration_date.strftime('%Y-%m-%d %H:%M:%S') if self.expiration_date else None
        }