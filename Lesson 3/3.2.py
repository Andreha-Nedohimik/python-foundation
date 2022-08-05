def info(first_name, last_name, year_born, tonw, telephon_number, email):
    print(
        "Вас зовут " + first_name + " " + last_name + ", Вы родились " + year_born + ", проживаете в городе " + tonw + ", Ваш номер телефона и email " + telephon_number + " " + email + "")


f_n, l_n = input("Здравствуйте, введите ваши имя и фамилию: ").split()
y_b, t = input("День рождения и город, в котором вы живете: ").split()
t_n, e = input("А так же ваш номер телефона и email: ").split()
info(first_name=f_n, year_born=y_b, tonw=t, telephon_number=t_n, last_name=l_n, email=e)
