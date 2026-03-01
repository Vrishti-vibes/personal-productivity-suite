# modules/backup_manager.py
import shutil
import os

class BackupManager:
    def __init__(self, backup_dir=None):
        self.backup_dir = backup_dir  # optional

    def backup_file(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"{filepath} does not exist")

        # If backup_dir not given, create inside file's directory
        if self.backup_dir is None:
            base_dir = os.path.dirname(filepath)
            backup_dir = os.path.join(base_dir, "backup")
        else:
            backup_dir = self.backup_dir

        os.makedirs(backup_dir, exist_ok=True)

        filename = os.path.basename(filepath)
        destination = os.path.join(backup_dir, filename)

        shutil.copy(filepath, destination)

        return destination