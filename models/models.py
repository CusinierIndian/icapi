from sqlalchemy import Column, String, Boolean, Integer, Float, Date, Numeric
# from config import app
from config import app
from flask_sqlalchemy import SQLAlchemy 
import flask

db = SQLAlchemy(app)
Base = db.Model

class SubscribedUser(Base):
	__tablename__ = 'subscribed_user'
	
	def __init__(self):
		pass

	def __init__(self, id, email, isSubscribed):
		self.id = id
		self.email = email
		self.isSubscribed = isSubscribed

	id = Column(String(100), primary_key=True, nullable=False)
	email = Column(String(255), unique=True, nullable=False)
	isSubscribed = Column(Boolean, nullable=False)


class Careers(Base):
	__tablename__ = 'careers'

	def __init__(self):
		pass

	def __init__(self, id, name, email, phone, role):
		self.id = id
		self.name = name
		self.email = email
		self.phone = phone
		self.role = role

	id = Column(String(100), primary_key=True, nullable=False)
	name = Column(String(255), nullable=False)
	email = Column(String(255), unique=True, nullable=True)
	phone = Column(String(15), unique=True, nullable=False)
	role = Column(String(50), nullable=False)


class ContactUs(Base):
	__tablename__ = 'contact_us'

	def __init__(self, id, name, email, phone):
		self.id = id
		self.name = name
		self.email = email
		self.phone = phone

	id = Column(String(100), primary_key=True, nullable=False)
	name = Column(String(255), nullable=False)
	email = Column(String(255), unique=True, nullable=False)
	phone = Column(String(15), unique=True, nullable=False)


class CookBasicDetails(Base):
	__tablename__ = 'cook_basic_details'

	def __init__(self, id, companyId, name, phone, email, joiningDate, nativePlace, currentPlace, experience, cookStatus, leavingDate,dob, gender):
		self.id = id
		self.companyId = companyId
		self.name = name
		self.phone = phone
		self.email = email
		self.joiningDate = joiningDate
		self.nativePlace = nativePlace
		self.currentPlace = currentPlace
		self.experience = experience
		self.cookStatus = cookStatus
		self.leavingDate = leavingDate
		self.dob = dob
		self.gender = gender

	id = Column(String(100), primary_key=True, nullable=False)
	name = Column(String(255), nullable=False)
	phone = Column(String(15), unique=True, nullable=False)
	nativePlace = Column(String(255), nullable=False)
	currentPlace = Column(String(255), nullable=False)
	experience = Column(Float, nullable=False)
	cookStatus = Column(String(15), nullable=False)
	gender = Column(String(8), nullable=False)
	joiningDate = Column(String(20), nullable=False)
	leavingDate = Column(String(20), nullable=True)
	dob = Column(String(20), nullable=False)
	companyId = Column(String(15), unique=True, nullable=False)
	email = Column(String(30), unique=True, nullable=True)

class TemporaryBooking(Base):

	__tablename__ = 'temporary_booking'

	def __init__(self, id, customerName, customerLocation, customerPhone, customerEmail, customerPreference, isRequiredInMorning, isRequiredInEvening, numberOfMembers):
		self.id = id
		self.customerName = customerName
		self.customerLocation = customerLocation
		self.customerPhone = customerPhone
		self.customerEmail = customerEmail
		self.customerPreference = customerPreference
		self.isRequiredInMorning = isRequiredInMorning
		self.isRequiredInEvening = isRequiredInEvening
		self.numberOfMembers = numberOfMembers


	id = Column(String(100) , primary_key=True, nullable=False)
	customerName = Column(String(255), nullable=False)
	customerLocation = Column(String(255), nullable=False)
	customerPhone = Column(String(15), nullable=False, unique=True)
	customerEmail = Column(String(50), nullable=False,unique=True)
	customerPreference = Column(String(30), nullable=False)
	isRequiredInMorning = Column(Boolean, nullable=False)
	isRequiredInEvening = Column(Boolean, nullable=False)
	numberOfMembers = Column(Integer, nullable=False)




