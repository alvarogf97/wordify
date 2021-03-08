from flask import Blueprint
import random
from services.user_service.user_service_json import retrieve_by_id
from serializers import user_serializer


user_bp = Blueprint('user', __name__)


@user_bp.route('/users/<int:id>/phrases/random')
def phrases_random(id):
        """ return a random phrases of a given user **id**"""
        user = retrieve_by_id(id)
        user_phrases = user_serializer(user)['phrases']
        phrase = random.randrange(len(user_phrases))
        return phrase
