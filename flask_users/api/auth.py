from flask import Blueprint, jsonify, request
from sqlalchemy import exc, or_

from flask_users.api.models import User
from flask_users import db, bcrypt


auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/auth/register', methods=['POST','GET'])
def register_user():
    post_data = request.get_json()
    if not post_data:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 400
    username = post_data.get('username')
    email = post_data.get('email')
    password = post_data.get('password')

    try:
        # check for existing user
        user = User.query.filter(
            or_(User.username == username, User.email == email)).first()
        if not user:
            new_user = User(
                username=username,
                email=email,
                password=password
            )
            db.session.add(new_user)
            db.session.commit()
            # generate auth token
            auth_token = new_user.encode_auth_token(new_user.id)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': auth_token.decode()
            }
            return jsonify(response_object), 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Sorry. That user already exists.'
            }
            return jsonify(response_object),400
    # handle errors
    except (exc.IntegrityError, ValueError) as err:
        db.session.rollback()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload'
        }
        return jsonify(response_object), 400

@auth_blueprint.route('/auth/login', methods=['POST', 'GET'])
def login_user():
    post_data = request.get_json()
    if not post_data:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 400
    email = post_data.get('email')
    password = post_data.get('password')
    try:
        # fetch user data
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password,password):
            auth_token = user.encode_auth_token(user.id)
            if auth_token:
                response_object = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token.decode()
                }
                return jsonify(response_object), 200
        else:
            response_object = {
                'status':'fail',
                'message': 'User does not exist.'
            }
            return jsonify(response_object), 404
    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Please login again.'
        }
        return jsonify(response_object), 500

@auth_blueprint.route('/auth/logout', methods=['GET'])
def logout_user():
    # get auth token
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
        response = User.decode_auth_token(auth_token)
        if not isinstance(response, str):
            response_object = {
                'status': 'success',
                'message': 'Successfully logged out.'
            }
            return jsonify(response_object), 200
        else:
            response_object = {
                'status': 'fail',
                'message': response
            }
            return jsonify(response_object), 403
    else:
        response_object = {
            'status': 'fail',
            'message': 'Provide a valid auth token.'
        }
        return jsonify(response_object), 401

@auth_blueprint.route('/auth/status', methods=['GET'])
def get_user_status():
    # get auth tokne
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
        response = User.decode_auth_token(auth_token)
        if not isinstance(response, str):
            user = User.query.filter_by(id=response).first()
            response_object = {
                'status': 'success',
                'data': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'active': user.active,
                    'created_at': user.created_at
                }
            }
            return jsonify(response_object), 200
        response_object = {
            'status': 'fail',
            'message': response
        }
        return jsonify(response_object),401
    else:
        response_object = {
            'status': 'fail',
            'message': 'Provide a valid token.'
        }
        return jsonify(response_object), 401
