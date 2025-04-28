from flask import Flask, render_template, request, redirect, url_for, session
from app.auth.auth import Auth
from app.auth.verification import Verification

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

auth = Auth()
verification = Verification()

@app.route('/')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_credentials = {'username': username, 'password': password}
        
        if auth.login(user_credentials):
            return redirect(url_for('verify'))
        else:
            return "Login Failed", 401
    return render_template('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        code = request.form['code']
        user_id = session.get('user_id')
        
        if verification.verify_code(user_id, code):
            return redirect(url_for('home'))
        else:
            return "Verification Failed", 401
    return render_template('verify.html')

@app.route('/logout')
def logout():
    auth.logout()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)