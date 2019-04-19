from flask import Flask, jsonify

# initialize the app
app = Flask(__name__)

# set config
app.config.from_object('flask_users.config.DevelopmentConfig')

@app.route('/ping', methods=('GET',))
def ping_pong():
    return jsonify({
            'status': 'success',
            'message': 'pong!'
    })