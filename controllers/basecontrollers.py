from repository.dboperations import DBOperations

class BaseController:
	def __init__(self):
		self.dbConnection = DBOperations()


	def getDbConnection(self):
		return self.dbConnection

	# def getLengthOfTable(self, model):
	# 	self.getDbConnection().getLengthOfTable(model)		


	