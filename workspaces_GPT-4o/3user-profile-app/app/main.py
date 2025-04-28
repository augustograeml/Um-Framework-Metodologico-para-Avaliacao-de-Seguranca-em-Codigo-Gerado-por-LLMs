from flask import Flask, render_template, request, redirect, url_for
from forms import ProfileForm
from models import UserProfile, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/user_profiles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/profile/<int:user_id>', methods=['GET'])
def profile(user_id):
    user = UserProfile.query.get(user_id)
    return render_template('profile.html', user=user)

@app.route('/update_profile/<int:user_id>', methods=['GET', 'POST'])
def update_profile(user_id):
    user = UserProfile.query.get(user_id)
    form = ProfileForm(obj=user)
    if form.validate_on_submit():
        user.name = form.name.data
        user.bio = form.bio.data
        db.session.commit()
        return redirect(url_for('profile', user_id=user.id))
    return render_template('update_profile.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)