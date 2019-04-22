import os
import sys
import datetime

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate db
db = SQLAlchemy()

# factory function
def create_app():
    # instantiate app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')     
    app.config.from_object(app_settings)
    
    # setup extensions
    db.init_app(app)
    
    # register blueprints
    from flask_users.api.views import users_blueprint
    app.register_blueprint(users_blueprint)
    
    return app

