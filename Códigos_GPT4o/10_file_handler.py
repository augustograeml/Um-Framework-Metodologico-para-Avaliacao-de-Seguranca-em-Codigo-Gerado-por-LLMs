def get_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"