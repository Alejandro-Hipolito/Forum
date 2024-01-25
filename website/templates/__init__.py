#Setup app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234' #Encrypt/Secure data (cookies). Random string rn, just to try

    #SQLite configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #Initialize DB
    db.init_app(app)

    from .views import views
    from .auth import auth

    #Register the routes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app




