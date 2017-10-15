from flask import Flask, render_template
import config

app = config.create_app()
from routes.others import others
app.register_blueprint(others, url_prefix= '/ic')
from routes.admin import admin
app.register_blueprint(admin, url_prefix= '/ic/admin')
from routes.authentication import authentication
app.register_blueprint(authentication, url_prefix='/ic')

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	from models.models import db
	# print db.Model.metadata.tables
	db.create_all()
	app.run(debug=True)

