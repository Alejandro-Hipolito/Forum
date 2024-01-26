#-----------------WONT USE IT-------------------

from flask import Blueprint

#Define the blueprint of the app
views = Blueprint('views', __name__)

@views.route('/') #When go to "/" route, home function appears
def home():
    return "<h1>Test</h1>"