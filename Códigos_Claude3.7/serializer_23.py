class Serializer:
    def serialize(self, obj, file_path):
        import pickle
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)

    def deserialize(self, file_path):
        import pickle
        with open(file_path, 'rb') as file:
            return pickle.load(file)