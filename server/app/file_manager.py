import os
from werkzeug.utils import secure_filename
from flask import request
import flask
from . import app
from app.views import CRUDView
from app.models import Publication, Proposal, Resource, Draft
from app.config import Config
from weasyprint import HTML
import json 
import markdown 

class FileManager:
    """
    A class that manages file operations for the application.

    Attributes:
        base_folder (str): The base folder path for file operations.
        drafts_folder (str): The folder path for storing drafts.
        resources_folder (str): The folder path for storing resources.
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
        

        self.base_folder = Config.FLASK_APP_FS_ROOT
        self.drafts_folder = os.path.join(self.base_folder, 'drafts')    
        self.resources_folder = os.path.join(self.base_folder, 'resources')
        self.library_folder = os.path.join(self.base_folder, 'library')
        self.publications_folder = os.path.join(self.library_folder, 'publications')
        self.proposals_folder = os.path.join(self.library_folder, 'proposals')

        # Ensure directories exist
        os.makedirs(self.base_folder, exist_ok=True)
        os.makedirs(self.drafts_folder, exist_ok=True)
        os.makedirs(self.resources_folder, exist_ok=True)
        os.makedirs(self.publications_folder, exist_ok=True)
        os.makedirs(self.proposals_folder, exist_ok=True)

        # Create CRUDView instances for publications and proposals
        self.draft_view = CRUDView(model=Draft)
        self.publication_view = CRUDView(model=Publication)
        self.proposal_view = CRUDView(model=Proposal)
        self.resource_view = CRUDView(model=Resource)

    def create_pdf_from_html(self, html_content, output_path):
        """
        Creates a PDF file from the given HTML content.

        Args:
            html_content (str): The HTML content to convert to PDF.
            output_path (str): The path where the PDF file will be saved.
        """
        try:
            HTML(string=html_content).write_pdf(output_path)
            return True
        except Exception as e:
            print(f"Failed to create PDF: {e}")
            return False

    def upload_file(self, file, user_id, project_id, filename, file_data, file_type, file_id=None):

        
        s_filename = secure_filename(filename)
        if file_type == 'draft':
            view = self.draft_view
            user_folder = os.path.join(self.drafts_folder, str(user_id))

        elif file_type == 'resource':
            view = self.resource_view
            user_folder = os.path.join(self.resources_folder, str(user_id))  
        else:
            raise ValueError("Invalid file type")
        project_folder = os.path.join(user_folder, str(project_id))
        file_path = os.path.join(project_folder, s_filename)
        
        os.makedirs(project_folder, exist_ok=True)
        file.save(file_path)

        file_data['file_path'] = file_path
        if file_id is None:
            with app.app_context():
                view.post(request_data=file_data)
        else:
            with app.app_context():
                view.put(item_id=file_id, request_data=file_data)
        if file_type == 'draft':
            html_content = markdown.markdown(file_data['content']) 
            self.create_pdf_from_html(html_content, file_path.replace('.html', '.pdf'))

    def download_file(self, user_id, project_id, filename, file_type):
        user_folder = os.path.join(self.base_folder, str(user_id))
        project_folder = os.path.join(user_folder, str(project_id))
        file_path = os.path.join(project_folder, filename)
        
        if file_type not in ['draft', 'resource']:
            raise ValueError("Invalid file type")

        return file_path if os.path.exists(file_path) else None

    def delete_file(self, user_id, project_id, filename, file_type):
        user_folder = os.path.join(self.base_folder, str(user_id))
        project_folder = os.path.join(user_folder, str(project_id))
        file_path = os.path.join(project_folder, filename)
        
        if file_type not in ['draft', 'resource']:
            raise ValueError("Invalid file type")

        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        else:
            return False
    
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