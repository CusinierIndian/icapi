from flask import Flask, Blueprint, request, jsonify, render_template, flash
from transformer.transformers import ExceptionTransformers
from constants.constants import Constants
from werkzeug.exceptions import BadRequest
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, BadSignature, BadData
from config import app

others = Blueprint('others', __name__)
safeTimed = URLSafeTimedSerializer(app.config['SECRET_KEY'])

@others.route('/subscribe', methods=['POST'])
def subscribe():
	try:
		subscribedUser = request.get_json()
	except Exception as e:
		return jsonify(ExceptionTransformers().transformExceptionSubcribedUser(Constants.INVALID_INPUT, str(e), Constants.STATUS_FAILED))
	else:
		from controllers.controllers import SubscriptionController
		return jsonify(SubscriptionController().subscribe(subscribedUser))


@others.route('/careers', methods=['POST'])
def careers():
	try:
		careerDetails = request.get_json()
	except Exception as e:
		return jsonify(ExceptionTransformers().transformExceptionCareer(Constants.INVALID_INPUT, Constants.INVALID_JSON, Constants.STATUS_FAILED))
	else:
		from controllers.controllers import CareerController
		return jsonify(CareerController().insertUserInCareers(careerDetails))

@others.route('/contactus', methods=['POST'])
def contactUs():
	try:
		contactUsDetails = request.get_json()
	except Exception as e:
		return jsonify(ExceptionTransformers().transformExceptionContactUs(Constants.INVALID_INPUT, Constants.INVALID_JSON, Constants.STATUS_FAILED))
	else:
		from controllers.controllers import ContactUsController
		return jsonify(ContactUsController().insertContactUsDetails(contactUsDetails))

#Temporary Cook Booking
@others.route('/cookbooking', methods=['POST'])
def bookCook():
	try:
		cookBookingDetails = request.get_json()
	except Exception as e:
		return jsonify(ExceptionTransformers().transformException(Constants.INVALID_INPUT, Constants.INVALID_JSON, Constants.STATUS_FAILED))
	else:
		from controllers.controllers import BookingController
		return jsonify(BookingController().bookACook(cookBookingDetails))


#Temporary feedback api from customers
@others.route('/feedback', methods=['POST'])
def customerFeedback():
	try:
		feedback = request.get_json()
	except BadRequest as e:
		return jsonify(ExceptionTransformers().transformException(Constants.INVALID_INPUT, Constants.INVALID_JSON, Constants.STATUS_FAILED))
	else: 
		from controllers.controllers import FeedbackController
		feedbackResponse = FeedbackController().customerFeedBack(feedback)
		if feedbackResponse and feedbackResponse.get('notification').get('status') == 'Success':
			mail = Mail(app)
			with  app.app_context():
				with mail.connect() as conn:
					feedback = feedbackResponse.get('data').get('comments')[0].get('feedback')
					customerName = feedbackResponse.get('data').get('customerName')
					temp = {
						'feedbackId' : feedbackResponse.get('data').get('comments')[0].get('feedbackId')
					}
					token = safeTimed.dumps(temp)
					link = 'http://127.0.0.1:5000/ic/approve/'+token
					modifyLink = 'http://127.0.0.1:5000/ic/modify/'+token
					msg = Message(subject='Feedback Approval', recipients=['vin13.rai@gmail.com'], sender='indiancuisinier@gmail.com')
					msg.html = render_template('test.html', feedback = feedback, token = token, link = link, modifyLink = modifyLink, customerName = customerName)
					conn.send(msg)
		return jsonify(feedbackResponse)



#Retrieving feedback from customer
@others.route('/getfeedback', methods=['GET'])
def retreiveFeedback():
	from controllers.controllers import FeedbackController
	return jsonify(FeedbackController().getFeedbacks())	


@others.route('/approve/<token>')
def approveFeedback(token):
	try:
		approval = safeTimed.loads(token)
	except BadSignature as badRequest:
		return jsonify({'message': 'Invalid token'})
	else:
		from controllers.controllers import FeedbackController
		response = FeedbackController().approveFeedback(approval)
		if response:
			flash('Feedback is approved')
		return jsonify(response)







