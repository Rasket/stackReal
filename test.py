import unittest

class nodeManager():
	def __init__ (self, *values):
		self.data_all = []
		for val in values:
			self.data_all.append(val)
		self.head = len(self.data_all)
	
	def getElem(self):
		try:
			return self.data_all.pop()
		except:
			return None

	def addElem(self, data):
		self.head = len(self.data_all)
		self.data_all.append(data)

	def __str__(self):
		return self.data_all.__str__()


class TestnodeManager(unittest.TestCase):

	def setUp(self):
		self.stack = nodeManager()

	def test_add_node(self):
		self.stack.addElem(123)
		self.assertEqual(str(self.stack), '[123]')

	def test_get_elem(self):
		self.stack.addElem(123)
		self.assertEqual(self.stack.getElem(), 123)

def runResult():
	with open('123.txt', 'w') as f:
		#f.write(str(unittest.main()))
		f.write('123')
	return None


runResult()

with open('123.txt', 'w') as f:
	f.write('123')