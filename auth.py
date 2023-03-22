from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

USERS = {
    "test_user": generate_password_hash("test_one")
}

@auth.verify_password
def verify_password(username, password):
    if username in USERS and check_password_hash(USERS.get(username), password):
        return username

@app.route("/")
@auth.login_required
def index():
    return f"Hello {auth.current_user()}!"
