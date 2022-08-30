m_f_1 = open("Test3.txt", "r", encoding="utf-8")
m_f_2 = open("Test4.txt", "w", encoding="utf-8")
rus_num = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
for line in m_f_1.readlines():
    m_f_2.write(f"{rus_num.get(line.split()[0])} {' '.join(line.split()[1:3])}\n")
m_f_2.close()
m_f_1.close()