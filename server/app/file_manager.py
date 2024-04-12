import os
from werkzeug.utils import secure_filename
from flask import request
from app import app
from app.views import CRUDView
from app.models import Publication, Proposal, Resource
import app.config

class FileManager:
    def __init__(self):
        #base_directory
        #--resources
        #--library
        #----publications
        #----proposals
        
        self.base_folder = app.config.BASE_DIR
        self.resource_folder = os.path.join(self.base_folder, 'resources')
        self.library_folder = os.path.join(self.base_folder, 'library')
        self.publications_folder = os.path.join(self.library_folder, 'publications')
        self.proposals_folder = os.path.join(self.library_folder, 'proposals')

        # Ensure directories exist
        os.makedirs(self.resource_folder, exist_ok=True)
        os.makedirs(self.publications_folder, exist_ok=True)
        os.makedirs(self.proposals_folder, exist_ok=True)

        # Create CRUDView instances for publications and proposals
        self.publication_view = CRUDView()
        self.publication_view.model = Publication  # Replace with your Publication model
        self.proposal_view = CRUDView()
        self.proposal_view.model = Proposal  # Replace with your Proposal model
        self.resource_view = CRUDView()
        self.resource_view.model = Resource  # Replace with your Resource model

    def upload_file(self, file, team_name, project_name, filename, resource_data, resource_id=None):
        # Sanitize filename using Werkzeug's secure_filename
        s_filename = secure_filename(filename)
        
        # Construct file path for resource based on team and project
        team_folder = os.path.join(self.resource_folder, team_name)
        project_folder = os.path.join(team_folder, project_name)
        file_path = os.path.join(project_folder, s_filename)
        
        # Ensure directories exist
        os.makedirs(project_folder, exist_ok=True)

        # Save the uploaded file to the specified upload folder
        file.save(file_path)

        # Add the file path to the resource data (resource data is a dictionary, JSON)
        resource_data['file_path'] = file_path

        # check if resource exists
        if resource_id is None:
            # If no resource_id is provided, create a new resource
            with app.test_request_context():
                # only one request.json can exist per context
                request.json = resource_data
                # send HTTP POST request to /api/resources to 
                self.resource_view.post()
        else:
            # If a resource_id is provided, update the existing resource
            with app.test_request_context():
                request.json = resource_data
                self.resource_view.put(resource_id)

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

        # Call the appropriate method to create or update the publication in the database
        with app.test_request_context():
            request.json = publication_data
            if publication_id is None:
                self.publication_view.post()
            else:
                self.publication_view.put(publication_id)

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

        # Call the appropriate method to create or update the proposal in the database
        with app.test_request_context():
            request.json = proposal_data
            if proposal_id is None:
                self.proposal_view.post()
            else:
                self.proposal_view.put(proposal_id)