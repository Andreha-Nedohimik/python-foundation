from random import random

final_test = []
test_list = [int(random() * 20) + 1 for i in range(1, int(random() * 30 + 10))]
print(test_list)
for i in test_list:
    if test_list.count(i) == 1:
        final_test.append(i)
print(final_test)
