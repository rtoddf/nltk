class Hero:
	def __init__(self, name):
		self.name = name
		self.health = 100

	def eat(self, food):
		if(food == 'apple'):
			self.health -= 100
		elif(food == 'ham'):
			self.health += 20

Bob = Hero('Bob')
print 'name: ', Bob.name
print 'health: ', Bob.health

Bob.eat('apple')
print 'health after eating an apple: ', Bob.health

Bob.eat('ham')
print 'health after eating ham: ', Bob.health