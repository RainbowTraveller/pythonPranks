class Empl():
#Module and class name conflict, so changed to Empl
	def __init__(self,name="",age=""):
		print "------------Employee------------"
		'Employee class'
		self.name = name
		self.age = age

	def getAge(self):
		return self.age
	
	def getName(self):
		return self.name
		
