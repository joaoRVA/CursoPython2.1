# count() é um iterator do itertools - contador sem fim

# diferenças do range e do count
from itertools import count


c1 = count(step=8, start=8)
r1 = range(8, 100, 8)


print('count')
for c in c1:
    if c >= 100:
        break
    print(c)

print()
print("range")
for r in r1:
    print(r)
    