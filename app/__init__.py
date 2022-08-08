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
    column_id = db.Column(db.Integer, nullable=False)

class Columns(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    font = db.Column(db.String(50), nullable=False)

    def __init__(self, font):
        self.font = font

    def __repr__(self):
        return '<font %r>' % self.font

db.create_all()
db.session.commit()

column_one = Columns('Courier New')
column_two = Columns('Trebuchet MS')
column_three = Columns('Brush Script MT')
db.session.add(column_one)
db.session.add(column_two)
db.session.add(column_three)
db.session.commit()

from app import routes
