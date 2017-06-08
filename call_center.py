from datetime import datetime
import datetime
current_id = 0000000


class Call(object):
	def __init__(self, name, phone_number, reason):
		global current_id
		self.id = current_id
		self.name = name
		self.return_number = phone_number
		self.time_of_call = datetime.datetime.time(datetime.datetime.now())
		self.start_time = datetime.datetime.now()
		self.reason_for_call = reason
		current_id += 1
	def display(self):
		print "Call ID: " + str(self.id)
		print "Caller Name: " + self.name
		print "Caller Phone#: " + self.return_number
		print "Time call received: " + str(self.time_of_call)
		print "Reason for call: " + self.reason_for_call

class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = len(self.calls)
	def add(self, name, phone_number, reason):
		new_call = Call(name, phone_number, reason)
		self.calls += [new_call]
	def remove(self):
		self.calls.pop(0)
	def info(self):
		current_time = datetime.datetime.now()
		for callers in self.calls:
			print "Caller {} is calling from {} and has been in the cue for {} ".format(callers.name, callers.return_number, str(current_time - callers.start_time))
			#convert to timeobject

cc = CallCenter()

cc.add("Scott", "123-1234", "Help!")
cc.add("Rachel", "231-5123", "Help Now!")
cc.add("Michael", "908-1232", "Help Please!")



time2 = datetime.datetime.now()

time2str = datetime.datetime.strftime(time2, "%Y %-m %-d %-H %-M %-S %f")
