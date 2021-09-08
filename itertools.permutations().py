from itertools import permutations


string = list(permutations('HACK',2))
fine = []
for i in string:
    list ="".join(i)
    fine.append(list)
fine.sort()

print("\n".join(fine))