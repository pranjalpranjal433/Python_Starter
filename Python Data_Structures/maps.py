d={}

d['a']=1
print('a' in d)
print('b' in d)
print(d.keys())
print(d.values())
print(len(d))
d.pop('a')

# error
# d.pop('b')

d['b']=2
d['a']=3

for key,val in d.items():
	print(key,val)

from collections import OrderedDict

od = OrderedDict()
od['c'] = 3
od['a'] = 10
od['b'] = 2
od['d'] = 4
 
for key, value in od.items():
    print(key, value)

names = {10:'Alice' ,2:'John' ,4:'Peter' ,3:'Andrew' ,6:'Ruffalo' ,5:'Chris' }  
#print a sorted list of the keys  
print(sorted(names.keys())) 
print("names",names) 
#print the sorted list with items.  
print(sorted(names.items()))  