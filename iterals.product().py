from itertools import product
a = input().split()
A=[]
B=[]
for i in range(len(a)):
    s=int(a[i])
    A.append(s)

b = input().split()
for i in range(len(b)):
    s=int(b[i])
    B.append(s)

data = list(product(A,B))
for i in range(len(data)):
    print(data[i],end = ' ')