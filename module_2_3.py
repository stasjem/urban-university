'''
Цель: применить навыки создания цикла while, а так же применения операторов break и continue.

Задача "Нули ничто, отрицание недопустимо!":
Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Нужно выписывать из этого списка только положительные числа до тех пор, 
пока не встретите отрицательное или не закончится список (выход за границу).


Результат выполнения программы:
Исходные данные:
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

Вывод на консоль:
42
69
322
13
99

'''


my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
new_list = []

while i < len(my_list):
    list = my_list[i]
    if list > 0:
        new_list.append(list)
        i += 1
    elif list == 0:
        # continue
        i += 1
    else:
        break

print(new_list)
