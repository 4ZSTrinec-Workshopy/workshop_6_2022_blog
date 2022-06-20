from flask import Blueprint, render_template

from models.post import Post

index_bp = Blueprint("index", __name__, template_folder="/templates")

@index_bp.route("/")
def index():
    posts = Post.query.all()

    return render_template("index.html", posts=posts)