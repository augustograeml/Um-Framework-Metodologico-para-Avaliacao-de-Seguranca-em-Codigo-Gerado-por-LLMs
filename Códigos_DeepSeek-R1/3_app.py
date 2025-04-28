from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'database/user_profiles.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def profile():
    conn = get_db()
    user = conn.execute('SELECT * FROM profiles WHERE id = 1').fetchone()  # Assuming a single user with id 1
    conn.close()
    return render_template('profile.html', user=user)

@app.route('/update', methods=['POST'])
def update_profile():
    name = request.form['name']
    bio = request.form['bio']
    
    conn = get_db()
    conn.execute('UPDATE profiles SET name = ?, bio = ? WHERE id = 1', (name, bio))  # Assuming a single user with id 1
    conn.commit()
    conn.close()
    
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)