a=input()
print(a)
# a[0]='2'
# a=a[::-1]
print(a[0:1])
print(len(a))

# immutable 
a=a[0:1]+'2'+a[2:]
print(a)

a="abcbdf"
b="cbdd"
c="abcbdffzzz"
print(a.find(b))
print(a>c)