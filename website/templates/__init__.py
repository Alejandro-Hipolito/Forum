#Setup app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
DB_NAME = "database.db"
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    #SQLite configuration
    app.config['SECRET_KEY'] = '1234' #Encrypt/Secure data (cookies). Random string rn, just to try
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivar para evitar advertencias

    #Initialize DB
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import views
    from .auth import auth
    from .routes import api

    #Register the routes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')

    return app




