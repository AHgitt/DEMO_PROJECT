from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)

flask_app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password123@mysql-flask-app:3309/my_websites"
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_app.config['SECRET_KEY'] = '867f6d5jhkd86g1iubd'

db = SQLAlchemy(flask_app)

class Sites(db.Model):
    site_url = db.Column(db.String(50), primary_key=True)
    site_colour = db.Column(db.String(30), nullable=True)

    def __init__(self, site_url, site_colour):
        self.site_url = site_url
        self.site_colour = site_colour

    def __repr__(self):
        return '<site_url %r>' % self.site_url


db.create_all()
db.session.commit()

site = Sites('www.youtube.com', 'red')
db.session.add(site)
db.session.commit()

from app import routes
