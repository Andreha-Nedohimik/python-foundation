my_list = list(input())
i = 0
mem = None
while (i < len(my_list)) and (i+1 != len(my_list)):
    mem = my_list[i]
    my_list.insert(i, my_list[i+1])
    my_list.pop(i+2)
    i += 2
for el in my_list:
    print (el, end='')