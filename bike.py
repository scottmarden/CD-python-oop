class Bike(object):
	def __init__(self, price, max_speed):
		self.wheels = 2
		self.price = price
		self.speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print "Price: $" + str(self.price)
		print "Max speed: " + self.speed
		print "Total miles :" + str(self.miles)
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		self.miles -= 5
		return self

bike1 = Bike(200, "25mph")

bike2 = Bike(1000, "35mph")

bike3 = Bike(50, "15mph")


bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()
