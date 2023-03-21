import os

from flask import Flask, redirect, render_template, request, session, url_for
from markupsafe import escape

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

class User:
    def __init__(self, username, group):
        self.username = username
        self.group = group

def get_current_user():
    user = User("Test User", "Test Group")
    return user

def get_all_users():
    return [
        User("Test User 1", "Test Group1 "),
        User("Test User 2", "Test Group 2")
    ]

@app.route("/")
def index():
    if "username" in session:
        return f"Logged in as {session['username']}"
    return "You are not logged in"

@app.route("/user/<name>")
def show_user_profile(name):
    return render_template("hello.html", name=name)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return render_template("post.html", post_id=post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route("/me")
def me():
    user = get_current_user()
    return {
        "username": user.username,
        "group": user.group,
    }

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

@app.route("/all_users")
def users():
    users = get_all_users()
    return [user.username for user in users]

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404
