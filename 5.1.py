m_f = open("Test1.txt", "w+")
for a in input("Введите данные: ").split():
    m_f.write(f"{a}\n")
m_f.seek(0)
print(m_f.readlines())
m_f.close()
