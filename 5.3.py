m_f = open("Test2.txt", "r", encoding="utf-8")
for line in m_f.readlines():
    if float(line.split()[1]) < 20000:
        print(line.split()[0])
m_f.close()