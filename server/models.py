from datetime import datetime
from server.app import db

# Define SQLAlchemy models
class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(50), nullable=False, unique=True)
    Email = db.Column(db.String(100), nullable=False, unique=True)
    PasswordHash = db.Column(db.String(255), nullable=False)
    IsConfirmed = db.Column(db.Boolean, default=False)
    IsAdmin = db.Column(db.Boolean, default=False)
    RegistrationDate = db.Column(db.DateTime, default=datetime.utcnow)

class Team(db.Model):
    TeamID = db.Column(db.Integer, primary_key=True)
    TeamName = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.Text)
    CreatorID = db.Column(db.Integer, db.ForeignKey('user.UserID'), nullable=False)
    creator = db.relationship('User', backref='teams')

class Message(db.Model):
    MessageID = db.Column(db.Integer, primary_key=True)
    SenderID = db.Column(db.Integer, db.ForeignKey('user.UserID'), nullable=False)
    RecipientID = db.Column(db.Integer, db.ForeignKey('user.UserID'), nullable=False)
    Subject = db.Column(db.String(100))
    MessageText = db.Column(db.Text, nullable=False)
    SentDate = db.Column(db.DateTime, default=datetime.utcnow)

class Project(db.Model):
    ProjectID = db.Column(db.Integer, primary_key=True)
    ProjectName = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.Text)
    ResourceDir = db.Column(db.String(255), nullable=False)
    TeamID = db.Column(db.Integer, db.ForeignKey('team.TeamID'), nullable=False)
    CreatorID = db.Column(db.Integer, db.ForeignKey('user.UserID'), nullable=False)
    IsPrivate = db.Column(db.Boolean, default=False)
    team = db.relationship('Team', backref='projects')
    creator = db.relationship('User', backref='created_projects')

class Draft(db.Model):
    DraftID = db.Column(db.Integer, primary_key=True)
    DraftName = db.Column(db.String(100), nullable=False)
    Content = db.Column(db.Text, nullable=False)
    ProjectID = db.Column(db.Integer, db.ForeignKey('project.ProjectID'), nullable=False)
    CreatorID = db.Column(db.Integer, db.ForeignKey('user.UserID'), nullable=False)
    UploadDate = db.Column(db.DateTime, default=datetime.utcnow)

class Resource(db.Model):
    ResourceID = db.Column(db.Integer, primary_key=True)
    ResourceName = db.Column(db.String(100), nullable=False)
    FilePath = db.Column(db.String(255), nullable=False)
    ResourceType = db.Column(db.String(50), nullable=False)
    ProjectID = db.Column(db.Integer, db.ForeignKey('project.ProjectID'), nullable=False)
    CreatorID = db.Column(db.Integer, db.ForeignKey('user.UserID'), nullable=False)

class Task(db.Model):
    TaskID = db.Column(db.Integer, primary_key=True)
    TaskName = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.Text)
    ProjectID = db.Column(db.Integer, db.ForeignKey('project.ProjectID'), nullable=False)
    CreatorID = db.Column(db.Integer, db.ForeignKey('user.UserID'), nullable=False)
    DueDate = db.Column(db.DateTime)
    IsCompleted = db.Column(db.Boolean, default=False)

class Proposal(db.Model):
    ProposalID = db.Column(db.Integer, primary_key=True)
    ProposalTitle = db.Column(db.String(100), nullable=False)
    FilePath = db.Column(db.String(255), nullable=False)
    CreatorID = db.Column(db.Integer, db.ForeignKey('user.UserID'), nullable=False)
    SubmissionDate = db.Column(db.DateTime, default=datetime.utcnow)
    Flags = db.Column(db.Integer, nullable=False, default=0)

class Publication(db.Model):
    PublicationID = db.Column(db.Integer, primary_key=True)
    PublicationName = db.Column(db.String(100), nullable=False)
    FilePath = db.Column(db.String(255), nullable=False)
    ProjectID = db.Column(db.Integer, db.ForeignKey('project.ProjectID'), nullable=False)
    CreatorID = db.Column(db.Integer, db.ForeignKey('user.UserID'), nullable=False)
    PublicationDate = db.Column(db.DateTime, default=datetime.utcnow)
    Flags = db.Column(db.Integer, nullable=False, default=0)

