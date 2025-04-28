def restore_object(file_path):
    import pickle
    try:
        with open(file_path, 'rb') as file:
            obj = pickle.load(file)
        return obj
    except (FileNotFoundError, IOError, pickle.UnpicklingError) as e:
        print(f"Error restoring object from {file_path}: {e}")
        return None