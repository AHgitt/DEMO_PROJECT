from app import db

class Sites(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    site_url = db.Column(db.String(50), nullable=False)
    site_colour = db.Column(db.String(30), nullable=True)
    column_id = db.Column(db.Integer, nullable=False)

class Columns(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    font = db.Column(db.String(50), nullable=False)
