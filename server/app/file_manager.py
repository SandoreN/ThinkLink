import os
from werkzeug.utils import secure_filename


class FileManager:
    def __init__(self, base_folder):
        self.base_folder = base_folder

    def upload_file(self, file, team_name, project_name, filename):
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