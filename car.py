class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price=price
		if price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.display_all()
	def display_all(self):
		print "Price: $" + str(self.price)
		print "Speed: " + self.speed
		print "Fuel: " + self.fuel
		print "Mileage: " + self.mileage
		print "Tax: " + str(self.tax)

car1 = Car(2000, "35mph", "Full", "20mpg")
car2 = Car(10000, "50mph", "Near empty", "12mpg")
car3 = Car(3000, "20mph", "Half full", "25mpg")
car4 = Car(15000, "40mph", "Near full", "35mpg")
car5 = Car(1000, "5mph", "half empty", "10mpg")
car6 = Car(8000, "45mph", "Full", "30mpg")
