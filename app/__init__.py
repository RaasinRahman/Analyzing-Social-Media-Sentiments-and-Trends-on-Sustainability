from flask import Flask
from flask_cors import CORS
from app.models.database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    CORS(app)

    # Initialize the database
    init_db(app)

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app