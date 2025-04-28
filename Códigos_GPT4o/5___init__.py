from flask import Flask

app = Flask(__name__)

# Configuration settings can be added here
app.config.from_object('config')