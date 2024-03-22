from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from flask import jsonify

from app.models import *


def create_app(db_conn):
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = db_conn
    db.init_app(app)

    
    @app.route('/positions')
    def positions():
        positions = db.session.query(models.Position).all()
        positions_dicts = [position.to_dict() for position in positions]
        return jsonify(positions_dicts)

    return app