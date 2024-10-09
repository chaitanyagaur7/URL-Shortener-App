from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URLMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(512), unique=True, nullable=False)
    short_url = db.Column(db.String(6), unique=True, nullable=False)
