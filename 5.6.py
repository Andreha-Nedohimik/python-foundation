m_f = open("Test6.txt", "r", encoding="utf-8")
my_dict = {}
for line in m_f.readlines():
    predm, numbers = line.split(':')
    name_sum = sum(map(int, "".join([i for i in numbers if i == ' ' or '9' >= i >= '0']).split()))
    my_dict[predm] = name_sum
    print([i for i in numbers if i == ' ' or '9' >= i >= '0'])
print(f"{my_dict}")
m_f.close()