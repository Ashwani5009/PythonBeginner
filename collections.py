# collections : Counter , namedtuple , OrderedDict , defaultDict , deque

from collections import namedtuple
from collections import deque

a = "aaaaabbbcccccccdd"
# my_counter = Counter(a)

# print(my_counter)  # Counter({'c': 7, 'a': 5, 'b': 3, 'd': 2})
# print(my_counter.keys())  # dict_keys(['a', 'b', 'c', 'd'])
# print(my_counter.most_common(1))

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
# print(pt.x, pt.y)  # Point(x=1, y=-4)

d = deque()
d.append(1)
d.append(2)
d.append(3)

d.appendleft(4)

d.pop()
d.popleft()

d.extendleft([7, 8])
