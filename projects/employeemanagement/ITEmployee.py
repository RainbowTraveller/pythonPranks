from Employee import Empl

class ITEmpl(Empl):
	def __init__(self, name = "", age = "", post = "", salary = 0, platform = ""):
		print "----------ITEmployee-------"
		Empl.__init__(self, name, age)
		self.salary = salary
		self.post = post
		self.platform = platform

	
	def getSalary(self):
		return self.salary

	def getPost(self):
		return self.post
		
	def getPlatform(self):
		return self.platform
