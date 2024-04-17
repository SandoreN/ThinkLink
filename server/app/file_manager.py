import os
from werkzeug.utils import secure_filename
from flask import request
from app import app
from app.views import CRUDView
from app.models import Publication, Proposal, Resource
import app.config

class FileManager:
    """
    A class that manages file operations for the application.

    Attributes:
        base_folder (str): The base folder path for file operations.
        resource_folder (str): The folder path for storing resources.
        library_folder (str): The folder path for the library.
        publications_folder (str): The folder path for storing publications.
        proposals_folder (str): The folder path for storing proposals.
        publication_view (CRUDView): An instance of CRUDView for managing publications.
        proposal_view (CRUDView): An instance of CRUDView for managing proposals.
        resource_view (CRUDView): An instance of CRUDView for managing resources.
    """

    def __init__(self):
        """
        Initializes a new instance of the FileManager class.
        """
        #uploads
        #--resources
        #--library
        #----publications
        #----proposals

        self.base_folder = app.config.Config.APP_FS_ROOT
        self.resource_folder = os.path.join(self.base_folder, 'resources')
        self.library_folder = os.path.join(self.base_folder, 'library')
        self.publications_folder = os.path.join(self.library_folder, 'publications')
        self.proposals_folder = os.path.join(self.library_folder, 'proposals')

        # Ensure directories exist
        os.makedirs(self.resource_folder, exist_ok=True)
        os.makedirs(self.publications_folder, exist_ok=True)
        os.makedirs(self.proposals_folder, exist_ok=True)

        # Create CRUDView instances for publications and proposals
        self.publication_view = CRUDView(model=Publication)
        self.proposal_view = CRUDView(model=Proposal)
        self.resource_view = CRUDView(model=Resource)

    def upload_file(self, file, user_id, project_id, filename, resource_data, resource_id=None):
        """
        Uploads a file to the specified user and project folder.

        Args:
            file (FileStorage): The file to be uploaded.
            user_id (str): The ID of the user.
            project_id (str): The ID of the project.
            filename (str): The original filename of the file.
            resource_data (dict): The data associated with the resource.
            resource_id (str, optional): The ID of the resource. Defaults to None.
        """
        # Sanitize filename using Werkzeug's secure_filename
        s_filename = secure_filename(filename)
        
        # Construct file path for resource based on team and project
        user_folder = os.path.join(self.resource_folder, user_id)
        project_folder = os.path.join(user_folder, project_id)
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
            with app.app_context():
                # send HTTP POST request to /api/resources to 
                self.resource_view.post(request_data=resource_data)
        else:
            # If a resource_id is provided, update the existing resource
            with app.app_context():
                self.resource_view.put(item_id=resource_id, request_data=resource_data)

    def download_file(self, user_id, project_id, filename):
        """
        Downloads a file from the specified user and project folder.

        Args:
            user_id (str): The ID of the user.
            project_id (str): The ID of the project.
            filename (str): The filename of the file to be downloaded.

        Returns:
            str: The file path if the file exists, None otherwise.
        """
        # Construct path based on team and project
        user_folder = os.path.join(self.base_folder, user_id)
        project_folder = os.path.join(user_folder, project_id)
        file_path = os.path.join(project_folder, filename)
        
        # Check if file exists
        if os.path.exists(file_path):
            return file_path
        else:
            return None  # File not found

    def delete_file(self, user_id, project_id, filename):
        """
        Deletes a file from the specified user and project folder.

        Args:
            user_id (str): The ID of the user.
            project_id (str): The ID of the project.
            filename (str): The filename of the file to be deleted.

        Returns:
            bool: True if the file was deleted successfully, False otherwise.
        """
        # Construct path based on team and project
        user_folder = os.path.join(self.base_folder, user_id)
        project_folder = os.path.join(user_folder, project_id)
        file_path = os.path.join(project_folder, filename)
        
        # Delete the specified file from the upload folder
        if os.path.exists(file_path):
            os.remove(file_path)
            return True  # File deleted successfully
        else:
            return False  # File not found
    
    def publish_project_file(self, publication_data, publication_id=None):
        """
        Publishes a project file by creating a symbolic link in the publications folder.

        Args:
            publication_data (dict): The data associated with the publication.
            publication_id (str, optional): The ID of the publication. Defaults to None.
        """
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
        with app.app_context():
            if publication_id is None:
                self.publication_view.post(request_data=publication_data)
            else:
                self.publication_view.put(item_id=publication_id, request_data=publication_data)

    def create_proposal_file(self, proposal_data, proposal_id=None):
        """
        Creates a proposal file by creating a symbolic link in the proposals folder.

        Args:
            proposal_data (dict): The data associated with the proposal.
            proposal_id (str, optional): The ID of the proposal. Defaults to None.
        """
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
        with app.app_context():
            if proposal_id is None:
                self.proposal_view.post(request_data=proposal_data)
            else:
                self.proposal_view.put(item_id=proposal_id, request_data=proposal_data)