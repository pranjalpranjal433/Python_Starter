# duck typing
class Pycharm:

	def execute(self):
		print("Compiling")
		print("Running")

class Editor:

	def execute(self):
		print("Spell Check")

class Laptop:
	def code(self,ide):
		ide.execute()

ide=Pycharm()
lap1=Laptop()
lap1.code(ide)

# operator overloading
a=5
b="World"
# print(a+b)
# int is a class
print(int.__add__(a,6))
print(str.__add__("a",b))

class Student:

	def __init__(self,m1,m2):
		self.m1=m1
		self.m2=m2

	def __add__(self,other):
		m1=self.m1+other.m1
		m2=self.m2+other.m2
		s3=Student(m1,m2)
		return s3
	def __gt__(self,other):
		m1=self.m1+other.m1
		m2=self.m2+other.m2
		if m1>m2:
			return True
		else:
			return False
	def __str__(self):
		return '{} {}'.format(self.m1,self.m2)

s1=Student(1,1)
s2=Student(2,2)

s3=s1+s2
print(s3.m1)
print(s1>s2)
print(s3)

# Overriding

class Student:

	def __init__(self,m1,m2):
		self.m1=m1
		self.m2=m2

	def sum(self,a=None,b=None,c=None):
		if a!=None and b!=None and c!=None:
			return a+b+c
		elif a!=None and b!=None:
			return a+b
		else:
			return a
	# def sum(self,a,b,c):
	# 	return a+b+c 

	def show(self):
		print("class Student")
class Students:

	def show(self):
		print("class Students")

class B(Students):

	def show(self):
		print("class B")


# no method overloading
s1=Student(2,3)
print(s1.sum(1,1))
print(s1.sum(1,1,1))

#method overridig

b1=B()
b1.show()