from flask import jsonify, request
from app import app, db
from .models import User, Team, Message, Project, Draft, Resource, Task, Proposal, Publication

def get_all(model):
    return jsonify([item.serialize() for item in model.query.all()])

def get_one(model, item_id):
    item = model.query.get(item_id)
    if not item:
        return jsonify({'error': f'{model.__name__} not found'}), 404
    return jsonify(item.serialize())

def create(model, **kwargs):
    item = model(**kwargs)
    db.session.add(item)
    db.session.commit()
    return item

def update(model, item_id, **kwargs):
    item = model.query.get(item_id)
    if not item:
        return jsonify({'error': f'{model.__name__} not found'}), 404
    for key, value in kwargs.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(item.serialize())

def delete(model, item_id):
    item = model.query.get(item_id)
    if not item:
        return jsonify({'error': f'{model.__name__} not found'}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': f'{model.__name__} deleted successfully'}), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    return get_all(User)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return get_one(User, user_id)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    return create(User, **data)

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    return update(User, user_id, **data)

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete(User, user_id)


@app.route('/api/teams', methods=['GET'])
def get_teams():
    return get_all(Team)

@app.route('/api/teams/<int:team_id>', methods=['GET'])
def get_team(team_id):
    return get_one(Team, team_id)

@app.route('/api/teams', methods=['POST'])
def create_team():
    data = request.json
    return create(Team, **data)

@app.route('/api/teams/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    data = request.json
    return update(Team, team_id, **data)

@app.route('/api/teams/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    return delete(Team, team_id)


@app.route('/api/messages', methods=['GET'])
def get_messages():
    return get_all(Message)

@app.route('/api/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    return get_one(Message, message_id)

@app.route('/api/messages', methods=['POST'])
def create_message():
    data = request.json
    return create(Message, **data)

@app.route('/api/messages/<int:message_id>', methods=['PUT'])
def update_message(message_id):
    data = request.json
    return update(Message, message_id, **data)

@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    return delete(Message, message_id)


@app.route('/api/projects', methods=['GET'])
def get_projects():
    return get_all(Project)

@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    return get_one(Project, project_id)

@app.route('/api/projects', methods=['POST'])
def create_project():
    data = request.json
    return create(Project, **data)

@app.route('/api/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.json
    return update(Project, project_id, **data)

@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    return delete(Project, project_id)


@app.route('/api/drafts', methods=['GET'])
def get_drafts():
    return get_all(Draft)

@app.route('/api/drafts/<int:draft_id>', methods=['GET'])
def get_draft(draft_id):
    return get_one(Draft, draft_id)

@app.route('/api/drafts', methods=['POST'])
def create_draft():
    data = request.json
    return create(Draft, **data)

@app.route('/api/drafts/<int:draft_id>', methods=['PUT'])
def update_draft(draft_id):
    data = request.json
    return update(Draft, draft_id, **data)

@app.route('/api/drafts/<int:draft_id>', methods=['DELETE'])
def delete_draft(draft_id):
    return delete(Draft, draft_id)


@app.route('/api/resources', methods=['GET'])
def get_resources():
    return get_all(Resource)

@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    return get_one(Resource, resource_id)

@app.route('/api/resources', methods=['POST'])
def create_resource():
    data = request.json
    return create(Resource, **data)

@app.route('/api/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    data = request.json
    return update(Resource, resource_id, **data)

@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    return delete(Resource, resource_id)


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return get_all(Task)

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return get_one(Task, task_id)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.json
    return create(Task, **data)

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    return update(Task, task_id, **data)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return delete(Task, task_id)


@app.route('/api/proposals', methods=['GET'])
def get_proposals():
    return get_all(Proposal)

@app.route('/api/proposals/<int:proposal_id>', methods=['GET'])
def get_proposal(proposal_id):
    return get_one(Proposal, proposal_id)

@app.route('/api/proposals', methods=['POST'])
def create_proposal():
    data = request.json
    return create(Proposal, **data)

@app.route('/api/proposals/<int:proposal_id>', methods=['PUT'])
def update_proposal(proposal_id):
    data = request.json
    return update(Proposal, proposal_id, **data)

@app.route('/api/proposals/<int:proposal_id>', methods=['DELETE'])
def delete_proposal(proposal_id):
    return delete(Proposal, proposal_id)


@app.route('/api/publications', methods=['GET'])
def get_publications():
    return get_all(Publication)

@app.route('/api/publications/<int:publication_id>', methods=['GET'])
def get_publication(publication_id):
    return get_one(Publication, publication_id)

@app.route('/api/publications', methods=['POST'])
def create_publication():
    data = request.json
    return create(Publication, **data)

@app.route('/api/publications/<int:publication_id>', methods=['PUT'])
def update_publication(publication_id):
    data = request.json
    return update(Publication, publication_id, **data)

@app.route('/api/publications/<int:publication_id>', methods=['DELETE'])
def delete_publication(publication_id):
    return delete(Publication, publication_id)