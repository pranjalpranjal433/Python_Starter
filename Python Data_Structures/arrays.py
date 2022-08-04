
a=[1,2,3]
print(a[0])
a.append(0)
print(a)
b=a.copy()
c=a
b[0]=10
c[0]=10
print(b,a,c)

