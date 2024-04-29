from flask import request, jsonify, send_from_directory, url_for, Blueprint, current_app, session
from . import app
from .models import Project, User, Team, Draft, Task, Resource, Message, Publication, Proposal
from .views import CRUDView
from .file_manager import FileManager
from app.config import Config
import logging
import json

logging.basicConfig(level=logging.DEBUG)
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

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/files/<path:filename>')
def serve_file(filename):
    return send_from_directory(Config.FLASK_APP_FS_ROOT, filename)

@routes_bp.route('/test', methods=['GET'])
def test_route():
    print(f"Current user logged in: {session['user']} , Authenticated: {'user' in session}")
    return jsonify({'message': 'Test route'}), 200

@routes_bp.route('/projects/<int:user_id>', methods=['GET', 'POST'])
def get_user_projects(user_id):
    logging.info(f"get_user_projects called with user_id: {user_id}")
    if 'user' not in session:
        logging.error("No user logged in")
        return jsonify({'message': 'Unauthorized'}), 403
    else:
        if request.method == 'POST':
        # Check if the logged-in user is the one trying to create a project
            if session['user']['id'] != user_id:
                logging.error(f"Logged in user id {session['user']['id']} does not match requested user id {user_id}")
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
            created_project, status = project_view.post(new_project)

            # Return the new project
            return jsonify(created_project), 201
        else:  # GET method
            print(f"get_user_projects called with user_id: {user_id}")
            # Check if the logged-in user is trying to access their own projects
            if session['user']['id'] != user_id:
                return jsonify({'message': 'Unauthorized'}), 403

            # Get the current user
            user, status = user_view.get({'id': user_id}, serialized=False)

            # Get all projects for the user
            user_projects, status = project_view.get(filters={'creator_id': user_id}, serialized=False, all_matches=True)
            user_projects = [project.serialize() for project in user_projects]
            # Get all projects that belong to any team the user is a part of
            team_projects = [project.serialize() for team in user.teams for project in team.projects]

            all_projects = user_projects + team_projects
            return jsonify(all_projects)

@routes_bp.route('/project_workspace/<int:project_id>', methods=['GET', 'POST'])
def get_project_workspace(project_id):
    if request.method == 'POST':
        # Get the project
        project, status = project_view.get(item_id=project_id, serialized=False)

        # Check if the logged-in user is the owner of the project
        if session['user']['id'] != project.creator_id:
            return jsonify({'message': 'Unauthorized'}), 403

        # Get the file from the request, if one was included
        file = request.files['file'] if 'file' in request.files else None

        data = request.form.get('file_data')
        # Get the data from the request
        if data is not None:
            if isinstance(data, str):
                data = json.loads(data)
        else:
            data = request.get_json()

        # Use request.form to parse FormData
        action = request.form.get('action')

        if action is None:
            logging.debug('No action specified in request data')
            return jsonify({'message': 'No action specified in request data'}), 400

        logging.debug(f'action: {action}')

        if action == 'create_draft':
            logging.debug(f'data: {data}')
            logging.debug(f'file: {file}')
            # Use file_manager.py to upload a new draft
            file_data = request.form.get('file_data')
            
            if file_data is None:
                return jsonify({'message': 'No file data included in request'}), 666
            else:
                #parse file_data back into a dictionary
                file_data = json.loads(file_data)
                file_data['project_id'] = project_id
                file_manager.upload_file(file, session['user']['id'], project_id, file_data['filename'], file_data, 'draft', file_id=None)
        elif action == 'create_task':
            # Use CRUDView to create a new task
            task_data = data.get('task_data')
            task_view.post(task_data)
        elif action == 'create_resource':
            # Use file_manager.py to upload a new resource
            resource_data = data.get('resource_data')
            file_manager.upload_file(resource_data['file'], session['user']['id'], project_id, resource_data['filename'], resource_data, 'resource', file_id=None)
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
        project, status = project_view.get({'id': project_id}, serialized=False)

        # Check if the logged-in user is the owner of the project
        if session['user']['id'] != project.creator_id:
            return jsonify({'message': 'Unauthorized'}), 403
        print(f"getting drafts and task for projects with project_id: {project_id}")
        # Get all drafts, tasks, and resources for the project
        drafts, status = draft_view.get(filters={'project_id': project_id}, all_matches=True)
        tasks, status = task_view.get(filters={'project_id': project_id}, all_matches=True)
        #resources, status = resource_view.get(filters={'project_id': project_id}, all_matches=True)

        #for resource in resources:
        #    resource['url'] = url_for('serve_file', filename=resource['filename'])
            
        # Get all users in the team the project belongs to
        #team_users = [user.serialize() for user in project.team.users]
        print(f'drafts: {drafts}')
        # Assuming drafts and tasks are 'Response' objects
        drafts_data = json.loads(drafts.get_data(as_text=True))
        tasks_data = json.loads(tasks.get_data(as_text=True))
        #resource_data = json.loads(resources.get_data(as_text=True))
        
        print(f'drafts_data: {drafts_data}')
        # Return the project workspace
        workspace_data = {
            'project': project.serialize(),
            'drafts': drafts_data,
            'tasks': tasks_data,
            #'resources': resources,
            #'team_users': team_users
        }
        return jsonify(workspace_data)
    
@routes_bp.route('/messages', methods=['POST'])
def send_message(message_data=None):
    message_view.post(message_data if message_data else request.get_json())
    return jsonify({'message': 'Message sent successfully'}), 201

@routes_bp.route('/messages/<int:receiver_id>', methods=['GET'])
def get_messages(receiver_id):
    messages, status = message_view.get(filters={'receiver_id': receiver_id}, serialized=False, all_matches=True)
    return jsonify([{'sender_id': msg.sender_id, 'subject': msg.subject, 'content': msg.content} for msg in messages])