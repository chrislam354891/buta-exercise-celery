from flask_restplus import Api

from .cats import api as api_ns_cats

api = Api()

api.add_namespace(api_ns_cats)
