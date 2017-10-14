from flask import Flask, Blueprint, request, jsonify, render_template
from transformer.transformers import ExceptionTransformers
from constants.constants import Constants
from werkzeug.exceptions import BadRequest

others = Blueprint('others', __name__)

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
		return jsonify(FeedbackController().customerFeedBack(feedback))

#Retrieving feedback from customer
@others.route('/getfeedback', methods=['GET'])
def retreiveFeedback():
	from controllers.controllers import FeedbackController
	return jsonify(FeedbackController().getFeedbacks())	







