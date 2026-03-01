# modules/file_organizer.py
import os

class FileOrganizer:
    def __init__(self, base_path="."):
        self.base_path = base_path

    def create_file(self, filename, content=""):
        path = os.path.join(self.base_path, filename)
        with open(path, "w") as f:
            f.write(content)
        return path

    def delete_file(self, filename):
        path = os.path.join(self.base_path, filename)
        if os.path.exists(path):
            os.remove(path)
            return True
        return False