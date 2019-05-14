import datetime

from flask_users import db 
from flask_users.api.models import User


def add_user(username, email, 
    password, created_at=datetime.datetime.utcnow()):
    user = User(
        username=username, 
        email=email, 
        password=password,
        created_at=created_at)
    db.session.add(user)
    db.session.commit()
    return user