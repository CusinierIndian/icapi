from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

# app = None
def create_app():
	global app
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'dev_IC'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///indiancuisinier.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['MAIL_SERVER']='smtp.gmail.com'
	app.config['MAIL_PORT'] = 465
	app.config['MAIL_USERNAME'] = 'indiancuisinier@gmail.com'
	app.config['MAIL_PASSWORD'] = 'Qwerty#123'
	app.config['MAIL_USE_TLS'] = False
	app.config['MAIL_USE_SSL'] = True
	app.config['MAIL_DEFAULT_SENDER'] = 'indiancuisinier@gmail.com'
	return app