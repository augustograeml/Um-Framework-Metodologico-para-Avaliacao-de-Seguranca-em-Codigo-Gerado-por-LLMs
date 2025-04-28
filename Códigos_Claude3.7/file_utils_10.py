def file_exists(file_name):
    import os
    return os.path.isfile(file_name)

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()