import os
from werkzeug.utils import secure_filename
from flask import request
from app import app
from app.routes import create_resource, update_resource, create_publication, create_proposal, update_publication, update_proposal

class FileManager:
    def __init__(self, base_folder):
        self.base_folder = base_folder
        self.resource_folder = os.path.join(self.base_folder, 'resources')
        self.library_folder = os.path.join(self.base_folder, 'library')
        self.publications_folder = os.path.join(self.library_folder, 'publications')
        self.proposals_folder = os.path.join(self.library_folder, 'proposals')

        # Ensure directories exist
        os.makedirs(self.resource_folder, exist_ok=True)
        os.makedirs(self.publications_folder, exist_ok=True)
        os.makedirs(self.proposals_folder, exist_ok=True)

    def upload_file(self, file, team_name, project_name, filename, resource_data, resource_id=None):
        # Sanitize filename using Werkzeug's secure_filename
        s_filename = secure_filename(filename)
        
        # Construct path based on team and project
        team_folder = os.path.join(self.resource_folder, team_name)
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
    
    def publish_project_file(self, publication_data, publication_id=None):
        # Get the file path from the publication data
        file_path = publication_data['file_path']

        # Create a symbolic link in the library/publications directory
        publication_folder = os.path.join(self.publications_folder, str(publication_id))

        # Ensure directories exist
        os.makedirs(publication_folder, exist_ok=True)

        # Create symbolic link
        symlink_path = os.path.join(publication_folder, os.path.basename(file_path))
        if not os.path.exists(symlink_path):
            os.symlink(file_path, symlink_path)

        # Call the appropriate function to create or update the publication in the database
        with app.test_request_context():
            request.json = publication_data
            if publication_id is None:
                create_publication()
            else:
                # I need to figure these out. should be ok though, I hope.
                update_publication(publication_id)

    def create_proposal_file(self, proposal_data, proposal_id=None):
        # Get the file path from the proposal data
        file_path = proposal_data['file_path']

        # Create a symbolic link in the library/proposals directory
        proposal_folder = os.path.join(self.proposals_folder, str(proposal_id))

        # Ensure directories exist
        os.makedirs(proposal_folder, exist_ok=True)

        # Create symbolic link
        symlink_path = os.path.join(proposal_folder, os.path.basename(file_path))
        if not os.path.exists(symlink_path):
            os.symlink(file_path, symlink_path)

        # Call the appropriate function to create or update the proposal in the database
        with app.test_request_context():
            request.json = proposal_data
            if proposal_id is None:
                create_proposal()
            else:
                #not too sure what's going on here
                update_proposal(proposal_id)