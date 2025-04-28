class BackupSaver:
    import pickle

    @staticmethod
    def save(obj, filename):
        with open(filename, 'wb') as file:
            BackupSaver.pickle.dump(obj, file)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as file:
            return BackupSaver.pickle.load(file)