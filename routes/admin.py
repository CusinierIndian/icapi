from flask import Flask, Blueprint, request, jsonify, render_template, url_for
from flask_mail import Mail, Message
from decorators.decorators import async
from itsdangerous import URLSafeTimedSerializer
from config import app
import jwt

admin = Blueprint('admin', __name__)

safeTimed = URLSafeTimedSerializer(app.config['SECRET_KEY'])


@admin.route('/sendmail', methods=['POST'])
def sendMail():
	try:
		postMailData = request.get_json()
	except:
		return 'Invalid Json'
	else:
		from controllers.controllers import AdminController
		users = AdminController().getUsers(postMailData.get('user'))
		message = postMailData.get('message')
		subject = postMailData.get('subject')
		return sendAsyncEmail(message, subject, users)
		
@async
def sendAsyncEmail(message, subject, users):
	mail = Mail(app)
	with app.app_context():
		with mail.connect() as conn:
			for email in users:
				token = safeTimed.dumps(email)
				# link = url_for('unsubscribe', token=token, _external=True)
				link = 'http://127.0.0.1:5000/ic/admin/unsubscribe/'+token
				msg = Message(subject=subject, recipients=[email], body=message, sender='indiancuisinier@gmail.com')
				#msg.html = '<a href='+ link +'> Unsubscribed</a>' 
				msg.html = render_template('test.html')
				conn.send(msg)
	return 'message sent'

@admin.route('/unsubscribe/<token>')
def unsubscribe(token):

	return "Unsubscribing"

@admin.route('/cookbasic', methods=['POST'])
def addCookBasicDetails():
	try:
		cookBasicData = request.get_json()

	except Exception as e:
		return jsonify(e.message)

	else:
		from controllers.controllers import AdminController
		return jsonify(AdminController().addCookDetails(cookBasicData))


#Get cook details
@admin.route('/cookdetails', methods=['GET'])
def getCookDetails():
	queryParams = request.args
	from controllers.controllers import AdminController
	return jsonify(AdminController().getCookDetails(queryParams))

#Get all cook Details
@admin.route('/getallcooks', methods=['GET'])
def getAllCookDetails():
	accessToken = request.headers.get('access-token')
	return accessToken
 





