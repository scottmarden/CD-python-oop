class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print "Health: " + str(self.health)

class Dog(Animal):
	def pet(self):
		self.health += 5

class Dragon(Animal):
	def fly(self):
		self.health -= 10
	def disaplyHealth(self):
		self.displayHealth()
		print "I am a Dragon"

class Snake(Animal):
	def slither(self):
		self.health -= 1
	def eat(self):
		self.health += 10



#########

class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print "Health: " + str(self.health)

class Dog(Animal):
	def pet(self):
		self.health += 5

class Dragon(Animal):
	def fly(self):
		self.health -= 10
	def disaplyHealth(self):
		self.displayHealth()
		print "I am a Dragon"

class Snake(Animal):
	def slither(self):
		self.health -= 1
	def eat(self):
		self.health += 10
