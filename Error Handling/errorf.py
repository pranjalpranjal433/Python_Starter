# (compile , logical , run time)-types
# sytax - compile
# users mistake adding when needed to multiply- logical
# user giving wrong input divide by 0 , file not find - run time


a=5
b=int(input('enter'))
try:
	print("resource open")
	print(a/b)
	# print("resource closed")
except ZeroDivisionError as e:
	print("cannot divide by 0",e)
	# print("resource closed")
except ValueError as e:
	print("Invalid error",e)
	# print("resource closed")
except Exception as e:
	print("Something went ern",e)
	# print("resource closed")
finally:
	print("resource closed")




