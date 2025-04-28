from flask import Flask, render_template
from app.routes.commands import command_routes

app = Flask(__name__)

# Register the command routes
app.register_blueprint(command_routes)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)