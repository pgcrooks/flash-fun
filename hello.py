from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index Page</p>"

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

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404
