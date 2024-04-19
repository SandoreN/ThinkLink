from flask import request, jsonify, send_from_directory, url_for
from flask_login import current_user, login_required
from . import app
from .models import Project, User, Team, Draft, Task, Resource, Message, Publication, Proposal
from .views import CRUDView
from .file_manager import FileManager
import app.config

# Create CRUDView instance for Project model to interact with the database
project_view = CRUDView(model=Project)
user_view = CRUDView(model=User)
team_view = CRUDView(model=Team)
draft_view = CRUDView(model=Draft)
task_view = CRUDView(model=Task)
resource_view = CRUDView(model=Resource)
message_view = CRUDView(model=Message)
publication_view = CRUDView(model=Publication)
proposal_view = CRUDView(model=Proposal)
file_manager = FileManager()

@app.route('/files/<path:filename>')
def serve_file(filename):
    return send_from_directory(app.config.Config.APP_FS_ROOT, filename)

@app.route('/projects/<int:user_id>', methods=['GET', 'POST'])
@login_required
def get_user_projects(user_id):
    if request.method == 'POST':
        # Check if the logged-in user is the one trying to create a project
        if current_user.id != user_id:
            return jsonify({'message': 'Unauthorized'}), 403

        # Get the data from the request
        data = request.get_json()

        # Create a new project
        new_project = {
            'name': data['name'],
            'description': data['description'],
            'resource_dir': data['resource_dir'],
            'creator_id': user_id
        }

        # Add the new project to the database using CRUDView
        created_project = project_view.create(new_project)

        # Return the new project
        return jsonify(created_project), 201

    else:  # GET method
        # Check if the logged-in user is trying to access their own projects
        if current_user.id != user_id:
            return jsonify({'message': 'Unauthorized'}), 403

        # Get the current user
        user, status = user_view.get({'id': user_id}, serialized=False)

        # Get all projects for the user
        user_projects, status = project_view.get(filters={'creator_id': user_id}, all_matches=True)

        # Get all projects that belong to any team the user is a part of
        team_projects = [project.serialize() for team in user.teams for project in team.projects]

        all_projects = user_projects + team_projects
        return jsonify(all_projects)

@app.route('/project_workspace/<int:project_id>', methods=['GET', 'POST'])
@login_required
def get_project_workspace(project_id):
    if request.method == 'POST':
        # Get the project
        project = project_view.get({'id': project_id}, serialized=False)

        # Check if the logged-in user is the owner of the project
        if current_user.id != project.user_id:
            return jsonify({'message': 'Unauthorized'}), 403

        # Get the data from the request
        data = request.get_json()

        # Depending on the action specified in the request, perform the appropriate operation
        action = data.get('action')
        if action == 'create_draft':
            # Use file_manager.py to upload a new draft
            draft_data = data.get('draft_data')
            draft_view.post(draft_data)
        elif action == 'create_task':
            # Use CRUDView to create a new task
            task_data = data.get('task_data')
            task_view.post(task_data)
        elif action == 'create_resource':
            # Use file_manager.py to upload a new resource
            resource_data = data.get('resource_data')
            file_manager.upload_file(resource_data['file'], current_user.id, project_id, resource_data['filename'], resource_data)
        elif action == 'publish':
            # Use file_manager.py to publish the project
            publication_data = data.get('publication_data')
            file_manager.publish_project_file(publication_data)
        elif action == 'submit':
            # Use file_manager.py to submit the project as a proposal
            proposal_data = data.get('proposal_data')
            file_manager.create_proposal_file(proposal_data)
        else:
            return jsonify({'message': 'Invalid action'}), 400

        return jsonify({'message': 'Action performed successfully'}), 200
    else:  # GET method
        # Get the project
        project = project_view.get({'id': project_id}, serialized=False)

        # Check if the logged-in user is the owner of the project
        if current_user.id != project.user_id:
            return jsonify({'message': 'Unauthorized'}), 403

        # Get all drafts, tasks, and resources for the project
        drafts = draft_view.get(filters={'project_id': project_id}, all_matches=True)
        tasks = task_view.get(filters={'project_id': project_id}, all_matches=True)
        resources = resource_view.get(filters={'project_id': project_id}, all_matches=True)

        for resource in resources:
            resource['url'] = url_for('serve_file', filename=resource['filename'])
            
        # Get all users in the team the project belongs to
        team_users = [user.serialize() for user in project.team.users]

        # Return the project workspace
        workspace = {
            'project': project.serialize(),
            'drafts': drafts,
            'tasks': tasks,
            'resources': resources,
            'team_users': team_users
        }
        return jsonify(workspace)
    
@app.route('/messages', methods=['POST'])
def send_message():
    message_view.post()
    return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/messages/<int:receiver_id>', methods=['GET'])
def get_messages(receiver_id):
    messages = message_view.get(filters={'receiver_id': receiver_id}, all_matches=True)
    return jsonify([{'sender_id': msg.sender_id, 'subject': msg.subject, 'content': msg.content} for msg in messages])