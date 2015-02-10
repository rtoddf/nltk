class Ph:
	# constructor
	def __init__(self):
		self.y = 5
		# call the function from within the class
		# don't need to pass self if called here
		self.printHam()
		# z here, is a local var and is deleted after execution
		# thus it cannot be accessed outside of the class
		# z = 5 
	def printHam(self):
		print 'ham'

# create an instance of the class
x = Ph()
# call the function inside the class
# x.printHam()

# access y from the constructor
print x.y
# print x.z