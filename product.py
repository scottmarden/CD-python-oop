class Product(object):
	def __init__(self, price, item_name, weight, brand, cost):
		self.price = price
		self.name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = "for sale"
	def sell(self):
		self.status = "sold"
		return self
	def addTax(self, tax):
		self.price = self.price + (self.price*tax)
		return self
	def returnProduct(self, reason):
		if reason == "defective":
			self.status = "defective"
		elif reason == "in box":
			self.status = "for sale"
		elif reason == "opened":
			self.status = "used"
			self.price = self.price - (self.price*.20)
		return self
	def displayInfo(self):
		print "Price: $" + str(self.price)
		print "Item: " + self.name
		print "Weight: " + self.weight
		print "Brand: " + self.brand
		print "Cost: $" + self.cost
		print "Status: " + self.status
		return self

soup = Product(5, "Tomato Soup", "8oz", "Campbells", "1")
