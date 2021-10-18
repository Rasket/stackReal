#realization of stack on python

class nodeManager():
	def __init__ (self, *values):
		self.data_all = []
		for val in values:
			self.data_all.append(val)
		self.head = len(self.data_all)
	
	def getElem(self):
		return data_all.pop()

	def addElem(self, data):
		self.head = len(self.data_all)
		self.data_all.append(data)

	def __str__(self):
		return self.data_all.__str__()


cal = nodeManager(123)
cal.addElem(123)
print(cal)

