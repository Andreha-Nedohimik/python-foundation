from random import random

test_list = [int(random() * 100) + 1 for i in range(1, int(random() * 30 + 10))]
final_list = []

h = 0
print(test_list)
for i in test_list:
    if i > h:
        final_list.append(i)
    h = i
print(final_list)
