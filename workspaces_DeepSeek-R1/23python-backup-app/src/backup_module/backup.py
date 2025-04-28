class BackupManager:
    def __init__(self, backup_dir='data/backups'):
        self.backup_dir = backup_dir

    def save_object(self, obj, filename):
        import os
        import pickle

        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

        file_path = os.path.join(self.backup_dir, filename)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)

    def list_backups(self):
        import os

        return [f for f in os.listdir(self.backup_dir) if os.path.isfile(os.path.join(self.backup_dir, f))]