from functools import reduce
from operator import add

values = (30, 10, 25, 70, 100, 94)

print(sorted(values))
print(values)

print(min(values))
print(max(values))
print(sum(values))
print(reduce(add, values))
print(reversed(values))
print(tuple(reversed(values)))
print(values)
