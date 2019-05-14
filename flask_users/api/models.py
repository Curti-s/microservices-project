import datetime

from flask_users import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, 
        email, password, 
        created_at=datetime.datetime.utcnow()):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at