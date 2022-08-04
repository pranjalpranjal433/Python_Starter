i=5
p=1
print("LSB",i&(-i))
for j in range(3):
	x=p<<j
	print(i&x,end="")
print("")
b='101'
print(int(b,2))
n=5
print(bin(n))


