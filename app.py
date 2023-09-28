"""Flask app for Cupcakes"""
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///playlist_app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)

with app.app_context():
    # Create database tables
    db.create_all()

app.config["SECRET_KEY"] = "I'LL NEVER TELL!!"
debug = DebugToolbarExtension(app)
