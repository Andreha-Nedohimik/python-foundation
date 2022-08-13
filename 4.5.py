from random import random
from functools import reduce

new_list = [i for i in range(100, 1001) if i % 2 == 0]
summ = reduce(lambda x, y: x * y, new_list)
print(summ)