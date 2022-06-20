from sqlalchemy import desc
from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(256))
    content = db.Column(db.String(4096))

    def __init__(self, title, description, content):
        self.title = title
        self.description = description
        self.content = content