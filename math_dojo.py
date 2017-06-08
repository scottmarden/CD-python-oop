#Part 1

class MathDojo(object):
	def __init__(self):
		self.name = "MathDojo"
		self.total = 0
	def add(self, *args):
		self.total += sum(args)
		return self
	def subtract(self, *args):
		self.total -= sum(args)
		return self
	def result(self):
		print self.total


#Part 2

class MathDojo(object):
	def __init__(self):
		self.name = "MathDojo"
		self.total = 0
	def add(self, *args):
		for i in range(len(args)):
			print args[i]
			if type(args[i]) == list:
				temp_sum = 0
				print "It's a list!"
				for j in range(len(args[i])):
					temp_sum += args[i][j]
				print temp_sum
				self.total += temp_sum
			elif type(args[i]) == tuple:
				temp_sum = 0
				print "It's a tuple!"
				for j in range(len(args[i])):
					temp_sum += args[i][j]
				print temp_sum
				self.total += temp_sum
			elif type(args[i]) == int:
				print "It's an int!"
				self.total += args[i]
	def subtract(self, *args):
		for i in range(len(args)):
			print args[i]
			if type(args[i]) == list:
				temp_sum = 0
				print "It's a list!"
				for j in range(len(args[i])):
					temp_sum += args[i][j]
				print temp_sum
				self.total -= temp_sum
			elif type(args[i]) == int:
				print "It's an int!"
				self.total -= args[i]

md = MathDojo()
