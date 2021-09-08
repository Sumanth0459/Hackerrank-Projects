from itertools import combinations_with_replacement
A,n = input().split()
A = sorted(A)

string = list(combinations_with_replacement(A,int(n)))
string.sort()
final =[]
for i in string:
    string = "".join(i)
    final.append(string)
print("\n".join(final))