class RestoreManager:
    def __init__(self):
        self.restored_objects = []

    def restore_object(self, filename):
        import pickle
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                self.restored_objects.append(obj)
                return obj
        except (FileNotFoundError, IOError, pickle.UnpicklingError) as e:
            print(f"Error restoring object from {filename}: {e}")
            return None

    def list_restored_objects(self):
        return self.restored_objects