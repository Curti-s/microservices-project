import os
import sys
import datetime

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


# instantiate db
db = SQLAlchemy()

# instantiate flask migrate
migrate = Migrate()

# instantiate flask_bcrypt
bcrypt = Bcrypt()

# factory function
def create_app():
    # instantiate app
    app = Flask(__name__)

    # enable CORS
    CORS(app)
    
    # set config
    app_settings = os.getenv('APP_SETTINGS')     
    app.config.from_object(app_settings)
    
    # setup extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # register blueprints
    from flask_users.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    from flask_users.api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)    
    return app

