# Configuration settings for the application

import os

# Base directory of the application
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to the plugins directory
PLUGINS_DIR = os.path.join(BASE_DIR, 'plugins')

# Default values for application settings
DEFAULT_SETTINGS = {
    'plugin_load_timeout': 5,  # seconds
    'max_loaded_plugins': 10,
    'log_level': 'INFO',
}