from basecontrollers import BaseController 
from constants.constants import Constants
from transformer.transformers import ExceptionTransformers
from repository.dboperations import DBOperations
from utility.utilities import validateEmail, generateUniqueId
from config import app
import jwt



#Subcription controller
class SubscriptionController(BaseController):

	def __init__(self):
		pass

	def subscribe(self, subscribedUser):
		from utility.utilities import validateEmail, generateUniqueId
		from models.models import SubscribedUser
		subscriptionData =  SubscribedUser(str(generateUniqueId()), subscribedUser.get('email'), True)
		return DBOperations().susbscribe(subscriptionData)
	


#Admin Controller
class AdminController(BaseController):
	def __init__(self):
		self.dbConnection = DBOperations()

	def getUsers(self, userType):
		userList = []
		if userType == 'subscribers':
			from models.models import SubscribedUser
			modelList = self.dbConnection.getUsers(SubscribedUser)
			for user in modelList:
				userList.append(user.email)
			return userList


	def unsubscribeUser(self, email):
		response = self.dbConnection.unsubscribeUser(email)
		return response

	#insert cook basic details
	def addCookDetails(self, cookBasic):
		from utility.utilities import generateUniqueId, generateCompanyId
		from models.models import CookBasicDetails
		lengthOfTable = self.dbConnection.getLengthOfTable(CookBasicDetails)
		companyId = str(generateCompanyId(lengthOfTable))
		cookBasicDetails = CookBasicDetails(str(generateUniqueId()), companyId, cookBasic.get('name'), cookBasic.get('phone')
			, cookBasic.get('email') , cookBasic.get('joiningDate'), cookBasic.get('nativePlace'), cookBasic.get('currentPlace')
			, cookBasic.get('experience'), cookBasic.get('cookStatus'), cookBasic.get('leavingDate')
			, cookBasic.get('dob'), cookBasic.get('gender'))

		return (self.dbConnection.addCookBasicDetais(cookBasicDetails))

	#get cook details
	def getCookDetails(self, queryParams):
		from transformer.keytransformer import searchable
		from models.models import CookBasicDetails
		optAndCol = searchable(queryParams, CookBasicDetails)
		print optAndCol
		return self.dbConnection.getCookDetails(optAndCol)


	#get Admin users
	def getAdminUsers(self):
		return self.dbConnection.getAdminUsers()

				




#Career Controller 
class CareerController(BaseController):

	def __init__(self):
		self.dbConnection = DBOperations()

	def insertUserInCareers(self, userCareer):
		from utility.utilities import generateUniqueId
		from models.models import Careers
		phone = userCareer.get('phone')
		email = userCareer.get('email')
		career = Careers(str(generateUniqueId()), userCareer.get('name'), email, phone, userCareer.get('role'))
		return self.dbConnection.insertUserInCareers(career)

#ContactUs Controller 

class ContactUsController(BaseController):

	def __init__(self):
		self.dbConnection = DBOperations()

	def insertContactUsDetails(self, contactUsDetails):
		from utility.utilities import validateEmail, validatePhoneNumber, generateUniqueId
		# isEmailValidated = validateEmail(contactUsDetails.get('email'))
		# isPhoneValidated = validatePhoneNumber(contactUsDetails.get('phone'))
		from models.models import ContactUs
		contactUsModel = ContactUs(str(generateUniqueId()), contactUsDetails.get('name'), contactUsDetails.get('email'), contactUsDetails.get('phone'))
		return self.dbConnection.insertContactUsDetails(contactUsModel)
	


#Temporary controller for booking a cook
class BookingController(BaseController):
	def __init__(self):
		self.dbConnection = DBOperations()

	def bookACook(self, cookBookingDetails):
		from utility.utilities import validateEmail, generateUniqueId
		from models.models import TemporaryBooking
		isRequiredInMorning = False
		isRequiredInEvening = False
		if(cookBookingDetails.get('isRequiredInMorning') == 'yes'):
			 isRequiredInMorning = True
		if(cookBookingDetails.get('isRequiredInEvening') == 'yes'):
			isRequiredInEvening = True
		bookACook = TemporaryBooking(str(generateUniqueId()), cookBookingDetails.get('customerName')
			, cookBookingDetails.get('customerLocation'), cookBookingDetails.get('customerPhone')
			, cookBookingDetails.get('customerEmail'), cookBookingDetails.get('cookPreference')
			, isRequiredInMorning, isRequiredInEvening
			, cookBookingDetails.get('numberOfMembers'))

		return self.dbConnection.bookACook(bookACook)	

#Temporary Feedback controller
class FeedbackController(BaseController):
	
	def __init__(self):
		self.dbConnection = DBOperations()

	def customerFeedBack(self, feedback):

		return self.dbConnection.customerFeedback(feedback)

	#method to retreive feedback
	def getFeedbacks(self):
		response = self.dbConnection.getFeedbacks();
		feedbackList = []
		for cd in response:
			feedbackListInd = []
			for f in cd.feedback:
				if f.isApproved == True:
					feedbackListInd.append(f.feedback)
					feedbackListInd.reverse()
					for fl in feedbackList:
						if cd.id == fl.get('customerId'):
							print cd.customerName
							feedbackList.remove(fl)
						
					feedbackList.append({
							'customerId' : cd.id,
							'customerName' : cd.customerName,
							'latestComment' : feedbackListInd[0]
							})
		from transformer.transformers import Transformers
		return Transformers().transformGetFeedback(feedbackList, Constants.STATUS_SUCCESS, Constants.SUCCESS_CODE)

	#method to approve feedback
	def approveFeedback(self, approval):
		feedbackId = approval.get('feedbackId')
		return self.dbConnection.approveFeedback(feedbackId)

	#method to modify feedback
	def modifyFeedback(self, feedback, feedbackId):
		return self.dbConnection.modifyFeedback(feedback, feedbackId)

#Authentication Controller
class AuthenticationController(BaseController):

	def __init__(self):
		self.dbConnection = DBOperations()

	#method to register user
	def registerUser(self, userDetails):
		userType = userDetails.get('user')
		if(userType == 'admin'):
			from models.models import AdminUser
			adminUser = AdminUser(str(generateUniqueId()), userDetails.get('name'), userDetails.get('email')
				, userDetails.get('password'))
			return self.dbConnection.registerUser(adminUser)


	#method to verify email
	def verifyEmail(self, verifiedEmail):
		userType = verifiedEmail.get('user')
		if(userType == 'admin'):
			from models.models import AdminUser
			return self.dbConnection.verifyEmail(AdminUser, verifiedEmail.get('id'))

	#method to login
	def login(self, loginUser):
		email = loginUser.get('email')
		password = loginUser.get('password')
		userType = loginUser.get('user')
		if userType == 'admin':
			from models.models import AdminUser
			response = self.dbConnection.login(AdminUser,email, password)
			if(response.get('notification').get('status') == 'Success'):
				jwt_encoded = jwt.encode(response, app.config['SECRET_KEY'], algorithm='HS256')
				return {'access-token' : jwt_encoded}







		

















