next_id = 0001

class Patient(object):
	def __init__(self, name, *allergies):
		global next_id
		self.id = next_id
		self.name = name
		self.allgergies = [allergies]
		self.bed_num = "None"
		next_id += 1

class Hospital(object):
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.patients = []
		self.bed_list = []
		for i in range(capacity):
			self.bed_list += [i+1]
	def admit(self, name, *allergies):
		new_patient = Patient(name, allergies)
		if len(self.patients) < self.capacity:
			self.patients += [new_patient]
			new_patient.bed_num = self.bed_list.pop(0)
			print "Admission complete!"
		else:
			print "Admission denied, hospital full."
		return new_patient
	def discharge(self, name):
		for i in range(len(self.patients)):
			if name == self.patients[i].name:
				self.bed_list += [self.patients[i].bed_num]
				self.patients[i].bed_num = "None"
				self.patients.pop(i)
				print "Discharge complete!"
				break
			else:
				continue

h = Hospital("St. John's", 3)
h2 = Hospital("St Judes", 19)

h.admit("Scott", "powder", "trumps", "love")
h.admit("Steve", "latex", "friendship", "vegetables")
h.admit("Sam", "blueberries", "hate")
