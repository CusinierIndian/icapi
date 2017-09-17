import re, time, uuid
#validate_email
def validateEmail(email):
	if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None:
		return True
	else:
		return False

#validate_phonenumber
def validatePhoneNumber(phoneNumber):
	if re.search('^(?:\+?44)?[07]\d{9,13}$', phoneNumber):
		return True
	else:
		return False


#Generate Unique Id
def generateUniqueId():
	id = uuid.uuid4()
	print id
	return id

#Generate company Id
def generateCompanyId(length):
	from constants.constants import Constants 
	return  Constants().BASE_ID_COOK + length + 1

# #Check QueryParams
# def checkQueryParams(queryParams):







