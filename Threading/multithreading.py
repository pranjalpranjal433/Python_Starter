from threading import *
import time

class A(Thread):
	def run(self):
		for i in range(5):
			print("helloA")
			time.sleep(1) 

class B(Thread):
	def run(self):
		for i in range(5):
			print("helloB")
			time.sleep(1)

t1=A()
t2=B()

# not run method start internally calls run so run method only sould be used 
t1.start()
t2.start()

# else bye will be printed before thread finish work join to main thread
t1.join()
t2.join()

print("Bye")

