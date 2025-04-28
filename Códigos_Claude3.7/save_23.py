def save_object(obj, file_path):
    import pickle
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file)