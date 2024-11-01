from flask import Flask, jsonify
import os
import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    from project.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    return app

#print(app.config, file=sys.stderr)
