#realization of stack on python
import unittest


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


class TestnodeManager(unittest.TestCase):

	def setUp(self):
		self.stack = nodeManager()

	def test_add_node(self):
		self.assertEqual(str(self.stack.addElem(123)), '[123]')



cal = nodeManager(123)
print(str(cal))
cal.addElem(123)


