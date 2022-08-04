class Computer:

	def __init__(self,cpu,ram):
		self.cpu=cpu
		self.ram=ram
		self.lap=self.laptop() 
		print("constructor")

	def show(self):
		print(self.cpu)
		self.lap.show()

	class laptop:

		def __init__(self):
			self.brand="HPPPPP"
		def show(self):
			print(self.brand)

c1=Computer(1,1)
c2=Computer(2,2)
c1.show()
# inner class 
ic=Computer.laptop()
print(c1.lap.brand)