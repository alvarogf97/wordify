from flask import Blueprint, jsonify
from wordify import serializers



user_bp = Blueprint('user', __name__)

def userservice(identifier):
    return ' '

def serializer(user):
    return { }

@user_bp.route('/<int:identifier>/phrases')
def get_users_phrases(identifier):
    try:
        user = userservice(identifier)
    except Exception as e:
         return jsonify(error=str(e)), 404
        
    var = serializer(user)
    return var