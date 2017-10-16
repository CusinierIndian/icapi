from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from config import app

authentication = Blueprint('authentication', __name__)
safeTimed = URLSafeTimedSerializer(app.config['SECRET_KEY'])

#register user
@authentication.route('/register', methods=['POST'])
def registerUser():
	try:
		userDetails = request.get_json()
	except BadRequest as badRequest:
		badRequest.message
	else:
		from controllers.controllers import AuthenticationController
		response = AuthenticationController().registerUser(userDetails)
		if response:
			mail = Mail(app)
			with  app.app_context():
				with mail.connect() as conn:
					email = response.get('data').get('email')
					temp = {
						'id' : response.get('data').get('id'),
						'user' : 'admin'
					}
					token = safeTimed.dumps(temp)
					link = 'http://127.0.0.1:5000/ic/verifyemail/'+token
					msg = Message(subject='verification link', recipients=[email], sender='indiancuisinier@gmail.com')
					msg.html = '<a href='+ link +'> Click here to verify your email with Indian Cuisinier</a>'
					conn.send(msg)

		return jsonify(response)

#Verify email
@authentication.route('/verifyemail/<token>')
def verifyEmail(token):
	try:
		verifiedEmail = safeTimed.loads(token)
	except Exception as e:
		return e.message
	else:
		print verifiedEmail
		from controllers.controllers import AuthenticationController
		return jsonify(AuthenticationController().verifyEmail(verifiedEmail))

	

