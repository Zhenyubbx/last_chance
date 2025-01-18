from flask import Flask
from .config import Config
from .routes import main
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import logging
from logging.handlers import RotatingFileHandler

# Initialize app, database, and migration
# db = SQLAlchemy()
# migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    app.config.from_pyfile('config.py', silent=True)

    # db.init_app(app)
    # migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(main)

    # Logging setup
    if not app.debug:
        handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)

    return app
