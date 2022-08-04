class A:
	def __init__(self):
		print("A")
	def feature1(self):
		print("f1 working")

	def feature2(self):
		print("f2 working")

class B(A):
	def __init__(self):
		super().__init__()
		print("B")
	def feature3(self):
		print("f3 working")

	def feature4(self):
		print("f4 working")
# mult-level
class C(B):
	def feature5(self):
		print("f3 working")

	def feature6(self):
		print("f4 working")
class F():
	def __init__(self):
		print("F")
	def feature10(self):
		print("f3 working")
# Multipe
class D(A,F):
	# biaaed for left - same for method left one called MRO Method Resolution Order
	def __init__(self):
		super().__init__()
		super().feature1()
		print("D")
	def feature7(self):
		print("f3 working")

a1=A()

a1.feature1()
a1.feature2()

b1=B()

b1.feature1()
b1.feature3()
b1.feature4()

d1=D()