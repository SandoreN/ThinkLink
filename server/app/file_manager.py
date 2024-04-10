import os
from werkzeug.utils import secure_filename
from flask import request
from app import app
from app.routes import create_resource, update_resource

class FileManager:
    def __init__(self, base_folder):
        self.base_folder = base_folder

    def upload_file(self, file, team_name, project_name, filename, resource_data, resource_id=None):
        # Sanitize filename using Werkzeug's secure_filename
        s_filename = secure_filename(filename)
        
        # Construct path based on team and project
        team_folder = os.path.join(self.base_folder, team_name)
        project_folder = os.path.join(team_folder, project_name)
        file_path = os.path.join(project_folder, s_filename)
        
        # Ensure directories exist
        os.makedirs(project_folder, exist_ok=True)

        # Save the uploaded file to the specified upload folder
        file.save(file_path)

        # Add the file path to the resource data
        resource_data['file_path'] = file_path

        # Call the appropriate function to create or update the resource in the database
        if resource_id is None:
            # If no resource_id is provided, create a new resource
            with app.test_request_context():
                request.json = resource_data
                create_resource()
        else:
            # If a resource_id is provided, update the existing resource
            with app.test_request_context():
                request.json = resource_data
                update_resource(resource_id)

    def download_file(self, team_name, project_name, filename):
        # Construct path based on team and project
        team_folder = os.path.join(self.base_folder, team_name)
        project_folder = os.path.join(team_folder, project_name)
        file_path = os.path.join(project_folder, filename)
        
        # Check if file exists
        if os.path.exists(file_path):
            return file_path
        else:
            return None  # File not found

    def delete_file(self, team_name, project_name, filename):
        # Construct path based on team and project
        team_folder = os.path.join(self.base_folder, team_name)
        project_folder = os.path.join(team_folder, project_name)
        file_path = os.path.join(project_folder, filename)
        
        # Delete the specified file from the upload folder
        if os.path.exists(file_path):
            os.remove(file_path)
            return True  # File deleted successfully
        else:
            return False  # File not found