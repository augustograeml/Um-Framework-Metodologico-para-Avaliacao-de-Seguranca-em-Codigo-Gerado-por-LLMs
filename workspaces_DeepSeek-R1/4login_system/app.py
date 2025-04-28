from flask import Flask, render_template, request, redirect, url_for, flash
from database.db_operations import create_user_table, add_user, get_user
from auth.auth_operations import verify_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if verify_user(username, password):
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Invalid credentials. Please try again.', 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    create_user_table()
    app.run(debug=True)