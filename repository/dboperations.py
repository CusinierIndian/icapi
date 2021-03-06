from constants.constants import Constants
from models.models import SubscribedUser, ContactUs,Careers, CookBasicDetails, TemporaryBooking, CustomerDetailsTemp, Feedback, AdminUser, db
from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
class DBOperations:

	def __init__(self):
		self.session = db.session()
		from transformer.transformers import Transformers, ExceptionTransformers
		self.transformer = Transformers()
		self.exceptionTransformer = ExceptionTransformers()

	def susbscribe(self, subscriptionData):
		try:
			self.session.add(subscriptionData)
			self.session.commit()
		except Exception as e:
			return self.exceptionTransformer.transformExceptionSubcribedUser(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)
		else:
			return self.transformer.transformSubscribedUser(SubscribedUser.query.filter_by(id=subscriptionData.id).first(), Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE)

	def getUsers(self, model):
		try:
			if model == SubscribedUser:
				return model.query.filter_by(email=model.email).filter_by(isSubscribed=True).all()
		except Exception as e:
			return e.message

	def unsubscribeUser(self, email):
		try:
			response = SubscribedUser.query.filter_by(email=email).first()
			response.isSubscribed = False
			self.session.commit()

		except Exception as e:
			return self.exceptionTransformer.transformExceptionSubcribedUser(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)

		else:
			return self.transformer.transformSubscribedUser(SubscribedUser.query.filter_by(id=response.id).first(), Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE)


	#Inserting users in careers table
	def insertUserInCareers(self, careers):
		try:
			print careers
			self.session.add(careers)
			self.session.commit()
		except Exception as e:
			return self.exceptionTransformer.transformExceptionCareer(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)

		else:
			return self.transformer.transformCareer(Careers.query.filter_by(id=careers.id).first(), Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE)

	#Inserting Contact Us Details
	def insertContactUsDetails(self, contactUs):
		try:
			self.session.add(contactUs)
			self.session.commit()
		except Exception as e:
			return self.exceptionTransformer.transformExceptionContactUs(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)
		else:
			return self.transformer.transformContactUS(ContactUs.query.filter_by(id=contactUs.id).first(), Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE)


	#Inserting basic cook details
	def addCookBasicDetais(self, cookDetails):
		try:
			self.session.add(cookDetails)
			self.session.commit()
		except Exception as e:
			return e.message
		else:
			return self.transformer.transformCookBasicDetails(CookBasicDetails.query.filter_by(id=cookDetails.id).first(), Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE)


	#Get length of Table
	def getLengthOfTable(self, model):
		try:
			response = model.query.all()
		except  Exception as e:
			return -1
		else:
			return len(response)

	#Apply operations on Table
	def applyOperations(self, optAndCol, model):
		opt = optAndCol.get('operation')
		col = optAndCol.get('col')
		if opt == '=':
			try:
				response = model.query.filter(col == optAndCol.get('value')).all()
			except Exception as e:
				return e.message
			else:
				print response
				return response

		elif opt == 'ilike':
			try:
				response = model.query.filter(col.ilike(optAndCol.get('value'))).all()
			except Exception as e:
				return self.exceptionTransformer.transformException(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)
			else:
				return response


	#Get cook details
	def getCookDetails(self, optAndCol):
		if optAndCol :
			response = self.applyOperations(optAndCol, CookBasicDetails)
			return self.transformer.transformCookBasicDetailsList(response, Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE )
		else:
			response = CookBasicDetails.query.all()
			return self.transformer.transformCookBasicDetailsList(response, Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE )


	#Temporary cook booking
	def bookACook(self, cookBookingDetails):
		try:
			self.session.add(cookBookingDetails)
			self.session.commit()
		except Exception as e:
			return self.exceptionTransformer.transformException(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)

		else:
			return self.transformer.transformerBookACook(TemporaryBooking.query.filter_by(id=cookBookingDetails.id).first(), Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE)


	#Temporary customer feedback
	def customerFeedback(self, feedback):
		global customerId
		try:
			response = CustomerDetailsTemp.query.filter_by(customerPhone=feedback.get('customerPhone')).first()
			from utility.utilities import generateUniqueId
			if response is None:
				customerDetails = CustomerDetailsTemp(str(generateUniqueId())
				, feedback.get('customerName'), feedback.get('customerEmail'), feedback.get('customerPhone')
				, feedback.get('cookName'))
				customerId = str(generateUniqueId())
				comment = Feedback(customerId, customerDetails.id, feedback.get('feedback'))
				self.session.add(customerDetails)
				self.session.add(comment)
			else:
				customerId = response.id
				comment = Feedback(str(generateUniqueId()), customerId, feedback.get('feedback'))
				self.session.add(comment)
			self.session.commit()
			cust = CustomerDetailsTemp.query.filter_by(customerPhone=feedback.get('customerPhone')).first()
			return self.transformer.transformReviewInsert(cust, Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE)

		except Exception as e:
			return self.exceptionTransformer.transformException(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)

	#Retreive feedback
	def getFeedbacks(self):
		try:
			response = CustomerDetailsTemp.query.all()
		except Exception as e:
			return self.exceptionTransformer.transformException(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)
		else:
			return response	


	#Register User
	def registerUser(self, userDetails):
		try:
			self.session.add(userDetails)
			self.session.commit()
		except IntegrityError as integrityError:
			return self.exceptionTransformer.transformException(Constants.INTEGRITY_ERROR_CODE, integrityError.message, Constants.INTEGRITY_ERROR)
		except Exception as e:
			return self.exceptionTransformer.transformException(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)

		else:
			return self.transformer.transformerRegisterUser(userDetails.query.filter_by(id=userDetails.id).first(), Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE)


	#verify email
	def verifyEmail(self, model, id):
		try:
			response = model.query.filter_by(id=id).first()
			response.isEmailVerified = True
			self.session.commit()
		except Exception as e:
			return self.exceptionTransformer.transformException(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)	
		else:
			return response.isEmailVerified

	#approve feedback
	def approveFeedback(self, feedbackId):
		try:
			response = Feedback.query.filter_by(id=feedbackId).first()
			response.isApproved = True
			self.session.commit()
		except Exception as e:
			return self.exceptionTransformer.transformException(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)
		else:
			return 'The feedback has been approved'

	#modify feedback
	def modifyFeedback(self, feedback, feedbackId):
		try:
			response = Feedback.query.filter_by(id=feedbackId).first()
			response.isApproved = True
			response.feedback = feedback
			self.session.commit()
		except Exception as e:
			return self.exceptionTransformer.transformException(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)
		else:
			return 'The feedback was modified'

	#login
	def login(self,model, email, password):
		try:
			response = model.query.filter_by(email=email).first()
			if response:
				if response.password == password:
					return self.transformer.transformUser(response, Constants.STATUS_SUCCESS,Constants.SUCCESS_CODE)
				else:
					return self.exceptionTransformer.transformException(Constants.INVALID_PASSWORD_CODE, Constants.INVALID_PASSWORD, Constants.STATUS_FAILED)

			else:
				return self.exceptionTransformer.transformException(Constants.NO_USER_FOUND, Constants.USER_NOT_REGISTER, Constants.STATUS_FAILED)
		except Exception as e:
			return self.exceptionTransformer.transformException(Constants.DATABASE_ERROR, e.message, Constants.STATUS_FAILED)



	#get admin users
	def getAdminUsers(self):
		try:
			response = AdminUser.query.all()
		except Exception as e:
			return None
		else:
			return response















