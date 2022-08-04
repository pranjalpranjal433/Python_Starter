class Computer:
	# class variable
	wheels=4
	def __init__(self,cpu,ram):
		# object variables
		self.cpu=cpu
		self.ram=ram
		print("constructor")


	def config(self):
		# self refers to calling object
		print(self.cpu,self.ram)

	def comapre(self,other):
		# compring object variabes for diferent objects 
		if self.cpu==other.cpu:
			print("yes")
		else:
			print("no")
	#class method tp access class variables
	@classmethod
	def info(cls):
		return cls.wheels

	# cannot access class or objectvariables just to show info
	@staticmethod
	def infos():
		return "wheels"

# class cannot be empty pass should be used
class Empty_Class:
	pass


eo=Empty_Class()
print(id(eo))
#object creation
comp=Computer(1,1);
# class and static member calls
print(Computer.info())
print(Computer.infos(),comp.infos())

comp=Computer(1,1);
comp2=Computer(2,2);
print(type(comp))

# instance member calls
comp.config()
comp2.config()

Computer.config(comp)
comp.comapre(comp2)

# class member 
Computer.wheels=Computer.wheels+1
print(comp.wheels)

