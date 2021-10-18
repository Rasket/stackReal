#realization of stack on python
from test import runResult
from test import nodeManager
from flask import Flask
import threading

app = Flask(__name__)

t1 = threading.Thread(target=runResult)

t1.start()



cal = nodeManager(123)
print(cal.getElem())
cal.addElem(123)




@app.route('/')
def index():
	return '123'

app.run()

