from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest

authentication = Blueprint('authentication', __name__)

#register user
@authentication.route('/register', methods=['POST'])
def registerUser():
	try:
		userDetails = request.get_json()
	except BadRequest as badRequest:
		badRequest.message
	else:
		from controllers.controllers import AuthenticationController
		return jsonify(AuthenticationController().registerUser(userDetails))

