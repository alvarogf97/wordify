import json
import random
import flask
from wordify.handlers.users import user_bp


def make_app():
  """Builds flask app by including blueprints."""
  app = flask.Flask(__name__)
  app.register_blueprint(user_bp, url_prefix='/api/search')
  return app
