#realization of stack on python

class nodeManager(data):
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


cal = node(123)
cal.addElem()

