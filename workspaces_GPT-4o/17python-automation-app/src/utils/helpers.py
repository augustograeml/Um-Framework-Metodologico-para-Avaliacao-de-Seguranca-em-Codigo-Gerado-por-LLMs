def load_script(script_path):
    """Load a script from the given path."""
    with open(script_path, 'r') as file:
        return file.read()

def execute_script(script_content):
    """Execute the provided script content."""
    exec(script_content)

def handle_error(error):
    """Handle errors that occur during script execution."""
    print(f"An error occurred: {error}")

def provide_feedback(message):
    """Provide feedback to the user."""
    print(message)