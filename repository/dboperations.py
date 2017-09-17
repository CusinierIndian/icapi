from constants.constants import Constants
from models.models import SubscribedUser, ContactUs,Careers, CookBasicDetails, db
from sqlalchemy import update
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






