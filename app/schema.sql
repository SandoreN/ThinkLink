-- User information
CREATE TABLE User (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL UNIQUE,
    Email TEXT NOT NULL UNIQUE,
    PasswordHash TEXT NOT NULL,
    IsConfirmed BOOLEAN DEFAULT 0,
    IsAdmin BOOLEAN DEFAULT 0,
    RegistrationDate DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- User-created groups
CREATE TABLE Group (
    GroupID INTEGER PRIMARY KEY AUTOINCREMENT,
    GroupName TEXT NOT NULL,
    Description TEXT,
    CreatorID INTEGER NOT NULL,
    FOREIGN KEY (CreatorID) REFERENCES User(UserID)
);

-- Messages between users or groups
CREATE TABLE Message (
    MessageID INTEGER PRIMARY KEY AUTOINCREMENT,
    SenderID INTEGER NOT NULL,
    RecipientID INTEGER NOT NULL,
    Subject TEXT,
    MessageText TEXT NOT NULL,
    SentDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (SenderID) REFERENCES User(UserID),
    FOREIGN KEY (RecipientID) REFERENCES User(UserID)
);

-- Research projects
CREATE TABLE Project (
    ProjectID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProjectName TEXT NOT NULL,
    Description TEXT,
    ResourceDir TEXT NOT NULL, --Reference to directory in the file system
    GroupID INTEGER NOT NULL,
    CreatorID INTEGER NOT NULL,
    IsPrivate BOOLEAN DEFAULT 0,
    FOREIGN KEY (GroupID) REFERENCES Group(GroupID),
    FOREIGN KEY (CreatorID) REFERENCES User(UserID)
);

-- Group members contribution to the project
CREATE TABLE Draft (
    DraftID INTEGER PRIMARY KEY AUTOINCREMENT,
    DraftName TEXT NOT NULL,
    Content TEXT NOT NULL,
    ProjectID INTEGER NOT NULL,
    CreatorID INTEGER NOT NULL,
    UploadDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID),
    FOREIGN KEY (CreatorID) REFERENCES User(UserID)
);

-- References to uploaded resources for a project
CREATE TABLE Resource (
    ResourceID INTEGER PRIMARY KEY AUTOINCREMENT,
    ResourceName TEXT NOT NULL,
    FilePath TEXT NOT NULL, -- Reference to the file in the file system
    ResourceType TEXT NOT NULL, -- e.g., 'dataset', 'image', 'document'
    ProjectID INTEGER NOT NULL,
    CreatorID INTEGER NOT NULL,
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID),
    FOREIGN KEY (CreatorID) REFERENCES User(UserID)
);

-- For task list in a project
CREATE TABLE Task (
    TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
    TaskName TEXT NOT NULL,
    Description TEXT,
    ProjectID INTEGER NOT NULL,
    CreatorID INTEGER NOT NULL,
    DueDate DATETIME,
    IsCompleted BOOLEAN DEFAULT 0,
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID),
    FOREIGN KEY (CreatorID) REFERENCES User(UserID)
);

-- Research proposals submitted by users
CREATE TABLE Proposal (
    ProposalID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProposalTitle TEXT NOT NULL,
    FilePath TEXT NOT NULL,
    CreatorID INTEGER NOT NULL,
    SubmissionDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Flags INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (CreatorID) REFERENCES User(UserID)
);

-- Completed projects (research papers) added to the public library
CREATE TABLE Publication (
    PublicationID INTEGER PRIMARY KEY AUTOINCREMENT,
    PublicationName TEXT NOT NULL,
    FilePath TEXT NOT NULL,
    ProjectID INTEGER NOT NULL,
    CreatorID INTEGER NOT NULL,
    PublicationDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Flags INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID),
    FOREIGN KEY (CreatorID) REFERENCES User(UserID)
);