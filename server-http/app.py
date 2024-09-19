from crypt import methods

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'

auth = HTTPBasicAuth()

# In-memory user database
users = {
    "admin": "secret",
    "user": "password"
}
api_token = 'Iephai6Uliechee9ahR7zo2u'

@auth.verify_password
def verify_password(username, password):
    if username in users.keys() and users[username] == password:
        session['username'] = username
        return username
    return None

@app.route('/', methods=['GET'])
def public_route():
    return jsonify({"message": "This is a public route"})

@app.route('/protected', methods=['GET'])
@auth.login_required
def protected_route():
    user = auth.current_user()
    session_info = {
        "session_id": request.cookies.get('session'),
        "username": session.get('username'),
        "remote_addr": request.remote_addr,
        "user_agent": request.user_agent.string
    }
    return jsonify({"message": f"Hello, {user}! This is a protected route.", "session_info": session_info})

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

    return render_template('login.html')

@app.route('/api', methods=['POST'])
def api():
    pass

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"message": "Unauthorized access"}), 401


if __name__ == '__main__':
    app.run(debug=True)

