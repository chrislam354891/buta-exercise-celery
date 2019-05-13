import flask
# from flask_restplus import Resource, Api

# from flask.ext.sqlalchemy import SQLAlchemy
from .celery.flaskcelery import FlaskCelery

celery = FlaskCelery()
# api = Api()

# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# More extensions below:
# db = SQLAlchemy()