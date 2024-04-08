from flask import jsonify, request
from app import app, db
from .models import User, Team, Message, Project, Draft, Resource, Task, Proposal, Publication
from .file_manager import FileManager
from .config import Config
from .auth import register_new_user


# Instantiate FileManager with the appropriate base folder
file_manager = FileManager(Config.UPLOAD_FOLDER)


# Routes for User CRUD operations
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.serialize())

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user_name = data['user_name']
    username = data['username']
    email_address = data['email_address']
    password = data['password']

    # Register the user
    new_user = register_new_user(user_name, username, email_address, password, is_confirmed=False, is_admin=False)

    return jsonify(new_user.serialize()), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    data = request.json
    user.user_name = data.get('user_name', user.user_name)
    user.username = data.get('username', user.username)
    user.email_address = data.get('email_address', user.email_address)
    user.password_hash = data.get('password_hash', user.password_hash)
    user.is_confirmed = data.get('is_confirmed', user.is_confirmed)
    user.is_admin = data.get('is_admin', user.is_admin)
    db.session.commit()
    return jsonify(user.serialize())

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

# Routes for Team CRUD operations
@app.route('/api/teams', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    return jsonify([team.serialize() for team in teams])

@app.route('/api/teams/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = Team.query.get(team_id)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    return jsonify(team.serialize())

@app.route('/api/teams', methods=['POST'])
def create_team():
    data = request.json
    new_team = Team(
        team_name=data['team_name'],
        team_description=data.get('team_description', ''),
        creator_id=data['creator_id']
    )
    db.session.add(new_team)
    db.session.commit()
    return jsonify(new_team.serialize()), 201

@app.route('/api/teams/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    team = Team.query.get(team_id)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    data = request.json
    team.team_name = data.get('team_name', team.team_name)
    team.team_description = data.get('team_description', team.team_description)
    db.session.commit()
    return jsonify(team.serialize())

@app.route('/api/teams/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    team = Team.query.get(team_id)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team deleted successfully'}), 200

# Routes for Message CRUD operations
@app.route('/api/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([message.serialize() for message in messages])

@app.route('/api/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = Message.query.get(message_id)
    if not message:
        return jsonify({'error': 'Message not found'}), 404
    return jsonify(message.serialize())

@app.route('/api/messages', methods=['POST'])
def create_message():
    data = request.json
    new_message = Message(
        sender_id=data['sender_id'],
        recipient_id=data['recipient_id'],
        message_subject=data.get('message_subject', ''),
        message_text=data['message_text']
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.serialize()), 201

@app.route('/api/messages/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    message = Message.query.get(message_id)
    if not message:
        return jsonify({'error': 'Message not found'}), 404
    data = request.json
    message.sender_id = data.get('sender_id', message.sender_id)
    message.recipient_id = data.get('recipient_id', message.recipient_id)
    message.message_subject = data.get('message_subject', message.message_subject)
    message.message_text = data.get('message_text', message.message_text)
    db.session.commit()
    return jsonify(message.serialize())

@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.query.get(message_id)
    if not message:
        return jsonify({'error': 'Message not found'}), 404
    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'Message deleted successfully'}), 200

# Routes for Project CRUD operations
@app.route('/api/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.serialize() for project in projects])

@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    return jsonify(project.serialize())

@app.route('/api/projects', methods=['POST'])
def create_project():
    data = request.json
    new_project = Project(
        project_name=data['project_name'],
        project_description=data.get('project_description', ''),
        resource_dir=data['resource_dir'],
        team_id=data['team_id'],
        creator_id=data['creator_id'],
        is_published=data.get('is_published', False),
        is_proposal=data.get('is_proposal', False)
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify(new_project.serialize()), 201

@app.route('/api/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    data = request.json
    project.project_name = data.get('project_name', project.project_name)
    project.project_description = data.get('project_description', project.project_description)
    project.resource_dir = data.get('resource_dir', project.resource_dir)
    project.team_id = data.get('team_id', project.team_id)
    project.creator_id = data.get('creator_id', project.creator_id)
    project.is_published = data.get('is_published', project.is_published)
    project.is_proposal = data.get('is_proposal', project.is_proposal)
    db.session.commit()
    return jsonify(project.serialize())

@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully'}), 200

# Routes for Draft CRUD operations
@app.route('/api/drafts', methods=['GET'])
def get_drafts():
    drafts = Draft.query.all()
    return jsonify([draft.serialize() for draft in drafts])

@app.route('/api/drafts/<int:draft_id>', methods=['GET'])
def get_draft(draft_id):
    draft = Draft.query.get(draft_id)
    if not draft:
        return jsonify({'error': 'Draft not found'}), 404
    return jsonify(draft.serialize())

@app.route('/api/drafts', methods=['POST'])
def create_draft():
    data = request.json
    new_draft = Draft(
        draft_name=data['draft_name'],
        draft_content=data['draft_content'],
        project_id=data['project_id'],
        creator_id=data['creator_id']
    )
    db.session.add(new_draft)
    db.session.commit()
    return jsonify(new_draft.serialize()), 201

@app.route('/api/drafts/<int:draft_id>', methods=['PUT'])
def update_draft(draft_id):
    draft = Draft.query.get(draft_id)
    if not draft:
        return jsonify({'error': 'Draft not found'}), 404
    data = request.json
    draft.draft_name = data.get('draft_name', draft.draft_name)
    draft.draft_content = data.get('draft_content', draft.draft_content)
    draft.project_id = data.get('project_id', draft.project_id)
    draft.creator_id = data.get('creator_id', draft.creator_id)
    db.session.commit()
    return jsonify(draft.serialize())

@app.route('/api/drafts/<int:draft_id>', methods=['DELETE'])
def delete_draft(draft_id):
    draft = Draft.query.get(draft_id)
    if not draft:
        return jsonify({'error': 'Draft not found'}), 404
    db.session.delete(draft)
    db.session.commit()
    return jsonify({'message': 'Draft deleted successfully'}), 200

# Routes for Resource CRUD operations
@app.route('/api/resources', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    return jsonify([resource.serialize() for resource in resources])

@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = Resource.query.get(resource_id)
    if not resource:
        return jsonify({'error': 'Resource not found'}), 404
    return jsonify(resource.serialize())

@app.route('/api/resources', methods=['POST'])
def create_resource():
    data = request.json
    uploaded_file = request.files['file']
    
    # Call FileManager's upload_file method
    file_manager.upload_file(
        file=uploaded_file,
        team_name=data['team_name'],
        project_name=data['project_name'],
        filename=uploaded_file.filename
    )

    # Create a new resource instance in the database
    new_resource = Resource(
        resource_name=data['resource_name'],
        file_path=uploaded_file.filename,  # Save the file path in the database
        resource_type=data['resource_type'],
        project_id=data['project_id'],
        creator_id=data['creator_id']
    )

    db.session.add(new_resource)
    db.session.commit()
    return jsonify(new_resource.serialize()), 201

@app.route('/api/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    resource = Resource.query.get(resource_id)
    if not resource:
        return jsonify({'error': 'Resource not found'}), 404
    data = request.json
    resource.resource_name = data.get('resource_name', resource.resource_name)
    resource.resource_type = data.get('resource_type', resource.resource_type)
    resource.project_id = data.get('project_id', resource.project_id)
    resource.creator_id = data.get('creator_id', resource.creator_id)
    db.session.commit()
    return jsonify(resource.serialize())

@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    resource = Resource.query.get(resource_id)
    if not resource:
        return jsonify({'error': 'Resource not found'}), 404
    
    # Call FileManager's delete_file method
    if file_manager.delete_file(resource.team_name, resource.project_name, resource.file_path):
        db.session.delete(resource)
        db.session.commit()
        return jsonify({'message': 'Resource deleted successfully'}), 200
    else:
        return jsonify({'error': 'File not found'}), 404

# Routes for Task CRUD operations
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.serialize() for task in tasks])

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task.serialize())

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(
        task_name=data['task_name'],
        task_description=data.get('task_description', ''),
        project_id=data['project_id'],
        creator_id=data['creator_id'],
        due_date=data.get('due_date', None),
        is_completed=data.get('is_completed', False)
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.serialize()), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    data = request.json
    task.task_name = data.get('task_name', task.task_name)
    task.task_description = data.get('task_description', task.task_description)
    task.project_id = data.get('project_id', task.project_id)
    task.creator_id = data.get('creator_id', task.creator_id)
    task.due_date = data.get('due_date', task.due_date)
    task.is_completed = data.get('is_completed', task.is_completed)
    db.session.commit()
    return jsonify(task.serialize())

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200

# Routes for Proposal CRUD operations
@app.route('/api/proposals', methods=['GET'])
def get_proposals():
    proposals = Proposal.query.all()
    return jsonify([proposal.serialize() for proposal in proposals])

@app.route('/api/proposals/<int:proposal_id>', methods=['GET'])
def get_proposal(proposal_id):
    proposal = Proposal.query.get(proposal_id)
    if not proposal:
        return jsonify({'error': 'Proposal not found'}), 404
    return jsonify(proposal.serialize())

@app.route('/api/proposals', methods=['POST'])
def create_proposal():
    data = request.formS
    new_proposal = Proposal(
        proposal_title=data['proposal_title'],
        file_path=data['file_path'],
        project_id=data['project_id'],
        creator_id=data['creator_id']
    )
    db.session.add(new_proposal)
    db.session.commit()
    return jsonify(new_proposal.serialize()), 201

@app.route('/api/proposals/<int:proposal_id>', methods=['PUT'])
def update_proposal(proposal_id):
    proposal = Proposal.query.get(proposal_id)
    if not proposal:
        return jsonify({'error': 'Proposal not found'}), 404
    data = request.form
    proposal.proposal_title = data.get('proposal_title', proposal.proposal_title)
    proposal.file_path = data.get('file_path', proposal.file_path)
    proposal.project_id = data.get('project_id', proposal.project_id)
    proposal.creator_id = data.get('creator_id', proposal.creator_id)
    proposal.flag_count = data.get('flag_count', proposal.flag_count)
    db.session.commit()
    return jsonify(proposal.serialize())

@app.route('/api/proposals/<int:proposal_id>', methods=['DELETE'])
def delete_proposal(proposal_id):
    proposal = Proposal.query.get(proposal_id)
    if not proposal:
        return jsonify({'error': 'Proposal not found'}), 404
    db.session.delete(proposal)
    db.session.commit()
    return jsonify({'message': 'Proposal deleted successfully'}), 200

## Routes for Publication CRUD operations
@app.route('/api/publications', methods=['GET'])
def get_publications():
    publications = Publication.query.all()
    return jsonify([publication.serialize() for publication in publications])

@app.route('/api/publications/<int:publication_id>', methods=['GET'])
def get_publication(publication_id):
    publication = Publication.query.get(publication_id)
    if not publication:
        return jsonify({'error': 'Publication not found'}), 404
    return jsonify(publication.serialize())

@app.route('/api/publications', methods=['POST'])
def create_publication():
    data = request.form
    new_publication = Publication(
        publication_title=data['publication_title'],
        file_path=data['file_path'],
        project_id=data['project_id'],
        creator_id=data['creator_id']
    )
    db.session.add(new_publication)
    db.session.commit()
    return jsonify(new_publication.serialize()), 201

@app.route('/api/publications/<int:publication_id>', methods=['PUT'])
def update_publication(publication_id):
    publication = Publication.query.get(publication_id)
    if not publication:
        return jsonify({'error': 'Publication not found'}), 404
    data = request.form
    publication.publication_title = data.get('publication_title', publication.publication_title)
    publication.file_path = data.get('file_path', publication.file_path)
    publication.project_id = data.get('project_id', publication.project_id)
    publication.creator_id = data.get('creator_id', publication.creator_id)
    publication.flag_count = data.get('flag_count', publication.flag_count)
    db.session.commit()
    return jsonify(publication.serialize())

@app.route('/api/publications/<int:publication_id>', methods=['DELETE'])
def delete_publication(publication_id):
    publication = Publication.query.get(publication_id)
    if not publication:
        return jsonify({'error': 'Publication not found'}), 404
    db.session.delete(publication)
    db.session.commit()
    return jsonify({'message': 'Publication deleted successfully'}), 200

