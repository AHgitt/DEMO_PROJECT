from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

flask_app = Flask(__name__)
time.sleep(10)
# flask_app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://flask:@db/my_websites"
flask_app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://{}:{}@{}/{}'.format('flask','password123','mysql','my_websites')
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_app.config['SECRET_KEY'] = '867f6d5jhkd86g1iubd'

db = SQLAlchemy(flask_app)

class Sites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_url = db.Column(db.String(50), nullable=False)
    site_colour = db.Column(db.String(30), nullable=False)
    row_id = db.Column(db.Integer, nullable=False)

class Rows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    font = db.Column(db.String(50), nullable=False)

    def __init__(self, font):
        self.font = font

    def __repr__(self):
        return '<font %r>' % self.font

db.create_all()
db.session.commit()

row_one = Rows('Courier New')
row_two = Rows('Trebuchet MS')
row_three = Rows('Brush Script MT')
db.session.add(row_one)
db.session.add(row_two)
db.session.add(row_three)
db.session.commit()

from app import routes
