class Store(object):
	def __init__(self, location, owner):
		self.loc = location
		self.owner = owner
		self.products = []
	def add_product(product):
		self.products += [product]
	def remove_product(product):
		if product in self.products:
			i = self.products.index(product)
			self.products.pop(i)
			return self.products
		else
			return self.products
	def inventory():
		for product in self.products:
			product.displayInfo
