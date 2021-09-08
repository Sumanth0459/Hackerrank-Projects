from itertools import combinations
input()
A = input().split()
n=int(input())
string = list(combinations(A,n))
a = len(string)
count = 0
for i in string:
    if 'a' in i:
        count+=1
print(round(count/a,3))