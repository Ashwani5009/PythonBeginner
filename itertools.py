# itertools : product , permutations , combinations , accumulate , groupby , and infinite iterators

from itertools import accumulate
import operator

a = [1, 2]
b = [3, 4]

# res = product(a, b)
# print(list(res)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

# perm = permutations(a)
# print(list(perm)) # [(1, 2), (2, 1)]

a = accumulate(a)  # default accumulate sum
a = accumulate(a, func=operator.mul)
