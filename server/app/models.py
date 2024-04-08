from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db
import datetime

class User(db.Model):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email_address = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    is_confirmed = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    registration_date = Column(DateTime, default=datetime.datetime.now())

    def serialize(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'username': self.username,
            'email_address': self.email_address,
            'is_confirmed': self.is_confirmed,
            'is_admin': self.is_admin,
            'registration_date': self.registration_date.strftime('%Y-%m-%d %H:%M:%S')
        }


class Team(db.Model):
    __tablename__ = 'Team'

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String(100), nullable=False)
    team_description = Column(Text)
    creator_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    creator = relationship('User', backref='teams')

    def serialize(self):
        return {
            'team_id': self.team_id,
            'team_name': self.team_name,
            'team_description': self.team_description,
            'creator_id': self.creator_id
        }


class Message(db.Model):
    __tablename__ = 'Message'

    message_id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    message_subject = Column(String(100))
    message_text = Column(Text, nullable=False)
    sent_date = Column(DateTime, default=datetime.datetime.now())

    def serialize(self):
        return {
            'message_id': self.message_id,
            'sender_id': self.sender_id,
            'recipient_id': self.recipient_id,
            'message_subject': self.message_subject,
            'message_text': self.message_text,
            'sent_date': self.sent_date.strftime('%Y-%m-%d %H:%M:%S')
        }

class Project(db.Model):
    __tablename__ = 'Project'

    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(100), nullable=False)
    project_description = Column(Text)
    resource_dir = Column(String(255), nullable=False)
    team_id = Column(Integer, ForeignKey('Team.team_id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    is_published = Column(Boolean, default=False)
    is_proposal = Column(Boolean, default=False)
    team = relationship('Team', backref='projects')
    creator = relationship('User', backref='created_projects')

    def serialize(self):
        return {
            'project_id': self.project_id,
            'project_name': self.project_name,
            'project_description': self.project_description,
            'resource_dir': self.resource_dir,
            'team_id': self.team_id,
            'creator_id': self.creator_id,
            'is_published': self.is_published,
            'is_proposal': self.is_proposal
        }


class Draft(db.Model):
    __tablename__ = 'Draft'

    draft_id = Column(Integer, primary_key=True)
    draft_name = Column(String(100), nullable=False)
    draft_content = Column(Text, nullable=False)
    project_id = Column(Integer, ForeignKey('Project.project_id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    upload_date = Column(DateTime, default=datetime.datetime.now())

    def serialize(self):
        return {
            'draft_id': self.draft_id,
            'draft_name': self.draft_name,
            'draft_content': self.draft_content,
            'project_id': self.project_id,
            'creator_id': self.creator_id,
            'upload_date': self.upload_date.strftime('%Y-%m-%d %H:%M:%S')
        }


class Resource(db.Model):
    __tablename__ = 'Resource'

    resource_id = Column(Integer, primary_key=True)
    resource_name = Column(String(100), nullable=False)
    file_path = Column(String(255), nullable=False)
    resource_type = Column(String(50), nullable=False)
    project_id = Column(Integer, ForeignKey('Project.project_id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)

    def serialize(self):
        return {
            'resource_id': self.resource_id,
            'resource_name': self.resource_name,
            'file_path': self.file_path,
            'resource_type': self.resource_type,
            'project_id': self.project_id,
            'creator_id': self.creator_id
        }

class Task(db.Model):
    __tablename__ = 'Task'

    task_id = Column(Integer, primary_key=True)
    task_name = Column(String(100), nullable=False)
    task_description = Column(Text)
    project_id = Column(Integer, ForeignKey('Project.project_id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    due_date = Column(DateTime)
    is_completed = Column(Boolean, default=False)

    def serialize(self):
        return {
            'task_id': self.task_id,
            'task_name': self.task_name,
            'task_description': self.task_description,
            'project_id': self.project_id,
            'creator_id': self.creator_id,
            'due_date': self.due_date.strftime('%Y-%m-%d %H:%M:%S') if self.due_date else None,
            'is_completed': self.is_completed
        }


class Proposal(db.Model):
    __tablename__ = 'Proposal'

    proposal_id = Column(Integer, primary_key=True)
    proposal_title = Column(String(100), nullable=False)
    file_path = Column(String(255), nullable=False)
    project_id = Column(Integer, ForeignKey('Project.project_id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    submission_date = Column(DateTime, default=datetime.datetime.now())
    flag_count = Column(Integer, nullable=False, default=0)

    def serialize(self):
        return {
            'proposal_id': self.proposal_id,
            'proposal_title': self.proposal_title,
            'file_path': self.file_path,
            'project_id': self.project_id,
            'creator_id': self.creator_id,
            'submission_date': self.submission_date.strftime('%Y-%m-%d %H:%M:%S'),
            'flag_count': self.flag_count
        }

class Publication(db.Model):
    __tablename__ = 'Publication'

    publication_id = Column(Integer, primary_key=True)
    publication_title = Column(String(100), nullable=False)
    file_path = Column(String(255), nullable=False)
    project_id = Column(Integer, ForeignKey('Project.project_id'), nullable=False)
    creator_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    publication_date = Column(DateTime, default=datetime.datetime.now())
    flag_count = Column(Integer, nullable=False, default=0)

    def serialize(self):
        return {
            'publication_id': self.publication_id,
            'publication_title': self.publication_title,
            'file_path': self.file_path,
            'project_id': self.project_id,
            'creator_id': self.creator_id,
            'publication_date': self.publication_date.strftime('%Y-%m-%d %H:%M:%S'),
            'flag_count': self.flag_count
        }