from crypt import methods

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_httpauth import HTTPBasicAuth
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

auth = HTTPBasicAuth()

# In-memory user database
users = {
    "admin": "secret",
    "user": "password"
}

@auth.verify_password
def verify_password(username, password):
    if username in users.keys() and users[username] == password:
        session['username'] = username
        return username
    return None

@app.route('/', methods=['GET', 'POST'])
def public_route():
    return jsonify({"message": "This is a public page"}), 200

@app.route('/protected', methods=['GET', 'POST'])
@auth.login_required
def protected_route():
    user = auth.current_user()
    session_info = {
        "session_id": request.cookies.get('session'),
        "username": session.get('username'),
        "remote_addr": request.remote_addr,
        "user_agent": request.user_agent.string
    }
    return jsonify({"message": f"Hello, {user}! This is a protected page.", "session_info": session_info}), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users.keys():
            if users[username] == password:
                return "Logged in successfully!"
        else:
            flash("Invalid username or password")

    return render_template('login.html'), 200

@app.route('/api', methods=['GET', 'POST'])
def print_request_info():
    api_output = {}

    api_output.update({'Header': dict(request.headers) })
    api_output.update({'GET': dict(request.args) })
    api_output.update({'POST': dict(request.form) })
    if request.is_json:
        api_output.update({'JSON Data': dict(request.get_json()) })
    api_output.update({'Session Data': dict(session) })
    return jsonify({"message": api_output}), 200

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"message": "Unauthorized access"}), 401


if __name__ == '__main__':
    app.run(debug=True)

