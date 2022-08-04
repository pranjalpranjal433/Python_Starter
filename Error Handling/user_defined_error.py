class BalanceException(Exception):
	pass

def check():
	a=1
	b=2
	try:
		c=a-b
		if(c<0):
			raise BalanceException('Insufficient')
	except BalanceException as e:
		print(e)

check()

def checkf():
	a=1
	b=2
	c=a-b
	if(c<0):
		raise BalanceException('Insufficient')
try:
	check()
except BalanceException as e:
	print(e)
