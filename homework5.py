'''
Практическое задание по теме: "Списки и словари"

Цель: Написать программу на языке Python, используя Pycharm, для работы со списками и словарями.

1. В проекте, где вы решаете домашние задания, создайте модуль 'homework5.py' и напишите весь код в нём.

2. Работа со списками:
  - Создайте переменную my_list и присвойте ей список из нескольких элементов, например, фруктов.
  - Выведите на экран список my_list.
  - Выведите на экран первый и последний элементы списка my_list.
  - Выведите на экран подсписок my_list с третьего до пятого элементов.
  - Измените значение третьего элемента списка my_list.
  - Выведите на экран измененный список my_list.
'''

my_list = ['banana', 'coconut', 'apple', 'cherry', 'raspberry']
print(my_list)
print(my_list[0]) # Выведите на экран первый элемент списка my_list.
print(my_list[-1]) # Выведите на экран и последний элементы списка my_list.
print(my_list[2:4]) # Выведите на экран подсписок my_list с третьего до пятого элементов.
my_list[2] = 'strawberry' # Измените значение третьего элемента списка my_list.
print(my_list)


'''
3. Работа со словарями:
  - Создайте переменную my_dict и присвойте ей словарь с парами ключ-значение, например, переводами некоторых слов.
  - Выведите на экран словарь my_dict.
  - Выведите на экран значение для заданного ключа в my_dict.
  - Измените значение для заданного ключа или добавьте новый в my_dict.
  - Выведите на экран измененный словарь my_dict.
'''
my_dict = { 'Nila': 373627676, 'Kira': 373627673826, 'Nikita': 383547676, 'Tina': 9876544576 }
print(my_dict)
print(my_dict['Tina']) # Выведите на экран значение для заданного ключа в my_dict.
my_dict['Tina'] = 123 # Измените значение для заданного ключа или добавьте новый в my_dict.
print(my_dict['Tina'])
my_dict['Karina'] = 292837363 # Добавьте новый в my_dict.
print(my_dict) # Выведите на экран измененный словарь my_dict.

