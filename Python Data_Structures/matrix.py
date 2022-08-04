R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
entries = list(map(int, input().split()))
a=[]

matrix=[]
for i in range(R):         
    a =[]
    for j in range(C):      
         a.append(int(input()))
    matrix.append(a)
  