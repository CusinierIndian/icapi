class Transformers:

	def __init__(self):
		pass

	def transformSubscribedUser(self, model, status, code):
		return {
			'data' :{
				'subscriberId' : model.id,
				'subscriberEmail' : model.email,
				'isSubscribed' : model.isSubscribed
			},
			'notification' : {
				'status' : status,
				'code' : code
			}
		}

	def transformContactUS(self, model, status, code):
		return {
			'data' :{
				'contactUsId' : model.id,
				'name' : model.name,
				'email' : model.email,
				'phone' : model.phone
			},
			'notification' : {
				'status' : status,
				'code' : code
			}
		}

	def transformCareer(self, model, status, code):
		return {
			'data': {
				'careerId' : model.id,
				'name' : model.name,
				'email' : model.email,
				'phone' : model.phone,
				'role' : model.role
			},
			'notification' : {
				'status' : status,
				'code' : code
			}
		}

	def transformCookBasicDetails(self, model, status, code):
		return {
			'data' : {
				'id' : model.id,
				'name' : model.name,
				'phone' : model.phone,
				'joiningDate' : model.joiningDate,
				'nativePlace' : model.nativePlace,
				'currentPlace' : model.currentPlace,
				'experience' : model.experience,
				'cookStatus' : model.cookStatus,
				'leavingDate' : model.leavingDate,
				'dob' : model.dob,
				'gender' : model.gender,
				'companyId' : model.companyId,
				'email' : model.email
			},
			'notification' : {
				'status' : status,
				'code' : code
			}
		}


class ExceptionTransformers:
	def __init__(self):
		pass


	def transformExceptionSubcribedUser(self, errorCode, errorMessage, status):
		return{
			'notification' : {
				'errorCode' : errorCode,
				'errorMessage' : errorMessage,
				'status' : status
			}
		}

	def transformExceptionContactUs(self, errorCode, errorMessage, status):
		return {
			'notification' : {
				'errorCode' : errorCode,
				'errorMessage' : errorMessage,
				'status' : status
			}
		}

	def transformExceptionCareer(self, errorCode, errorMessage, status):
		return {
			'notification' : {
				'errorCode' : errorCode,
				'errorMessage' : errorMessage,
				'status' : status
			}
		}

	def transformException(self, errorCode, errorMessage, status):
		return {
			'notification' : {
				'errorCode' : errorCode,
				'errorMessage' : errorMessage,
				'status' : status
			}
		}