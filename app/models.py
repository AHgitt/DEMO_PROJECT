from app import db

class Sites(db.Model):
    site_url = db.Column(db.String(50), primary_key=True)
    site_colour = db.Column(db.String(30), nullable=True)
