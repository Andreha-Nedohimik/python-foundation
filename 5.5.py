from random import random


def m_list(a):
    def_list = []
    p = random() * a
    while p > 0:
        def_list.append(str(random() * 50))
        p -= 1
    return (' '.join(def_list))


sum_number = 0
m_f = open("Test5.txt", "w+", encoding="utf-8")
m_f.write(m_list(60))
m_f.seek(0)
for number in m_f.readline().split():
    sum_number += float(number)
print(sum_number)
m_f.close()
