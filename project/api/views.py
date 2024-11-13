from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import exc
from project.api.models import User
from project import db

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@users_blueprint.route('/users', methods=['POST'])
def add_user():
    post_data = request.get_json()
    if not post_data:
        return jsonify({
            'status': 'fail',
            'message': 'Invalid payload.'
        }), 400
    email = post_data.get('email')
    username = post_data.get('username')
    try:
        user=User.query.filter_by(email=email).first()
        if not user:
            db.session.add(User(username=username, email=email))
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': f'{email} was added!'    
            }), 201
        else:
            return jsonify({
                'status': 'fail',
                'message': 'Sorry. That email already exists.'
            }), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify({
            'status': 'fail',
            'message': 'Invalid payload.'
        }), 400


