from flask import Blueprint, render_template, request

from models.post import Post

from app import db

posts_bp = Blueprint("posts", __name__, template_folder="/templates")

@posts_bp.route("/post/<int:id>")
def post(id):
    post = Post.query.filter(Post.id==id).one()

    return render_template("post.html", post=post)

@posts_bp.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("description")
        content = request.form.get("content")

        post = Post(title, desc, content)
        db.session.add(post)
        db.session.commit()

    return render_template("create_post.html")