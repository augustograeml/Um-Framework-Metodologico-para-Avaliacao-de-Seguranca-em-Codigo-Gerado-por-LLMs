def create_file(filename: str):
    with open(filename, 'w') as f:
        f.write('')

def delete_file(filename: str):
    import os
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")