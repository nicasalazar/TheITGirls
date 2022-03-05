from wsgiref.validate import validator
from flask import Flask

def create_app():
   app = Flask(__name__, template_folder='./views',static_folder='./static')

   with app.app_context():
        import routes.views

   return app


