class BackupRestorer:
    def restore(self, filename):
        import pickle
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, IOError) as e:
            print(f"Error restoring file: {e}")
            return None