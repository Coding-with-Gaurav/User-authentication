from flask import Flask, render_template, request, redirect, url_for, session
import os

from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
# port = int(os.environ.get('PORT', 5000))
# app.run(host='0.0.0.0', port=port)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']
collection = db['users']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Hash the password before storing it
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user_data = {'name': name, 'email': email, 'password': hashed_password}
        collection.insert_one(user_data)

        return redirect(url_for('index'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = collection.find_one({'email': email})

        if user and check_password_hash(user['password'], password):
            session['user'] = {'name': user['name'], 'email': user['email']}
            return redirect(url_for('my_details'))
        else:
            return render_template('login.html', error='Invalid email or password')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/my_details')
def my_details():
    users = collection.find()
    return render_template('my_details.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
