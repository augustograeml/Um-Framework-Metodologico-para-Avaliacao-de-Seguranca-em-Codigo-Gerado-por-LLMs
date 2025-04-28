class DynamicLoader:
    def __init__(self):
        self.loaded_libraries = {}

    def load_library(self, library_name):
        """Dynamically loads a user-provided library."""
        try:
            library = __import__(library_name)
            self.loaded_libraries[library_name] = library
            return library
        except ImportError as e:
            print(f"Error loading library '{library_name}': {e}")
            return None

    def unload_library(self, library_name):
        """Unloads a previously loaded library."""
        if library_name in self.loaded_libraries:
            del self.loaded_libraries[library_name]
            print(f"Library '{library_name}' has been unloaded.")
        else:
            print(f"Library '{library_name}' is not loaded.")