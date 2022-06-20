from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db = SQLAlchemy(app)

from models.post import Post

db.create_all()

from controllers.index_controller import index_bp
from controllers.post_controller import posts_bp

app.register_blueprint(index_bp)
app.register_blueprint(posts_bp)