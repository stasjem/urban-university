'''
Практическое задание
2023/12/26 00:00|Домашнее задание по теме "Интроспекция"
Цель задания:

Закрепить знания об интроспекции в Python.
Создать персональную функции для подробной интроспекции объекта.

Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).


Пример работы:
number_info = introspection_info(42)
print(number_info)

Вывод на консоль:
{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}

Рекомендуется создавать свой класс и объект для лучшего понимания

Файл с кодом прикрепите к домашнему заданию.
'''


def introspection_info(obj):

    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = vars(obj)
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    # callable() - можно ли вызвать.  getattr() - возвращает значение атрибута у объекта
    # startswith() - проверяет с какого префикса начинается
    info['module'] = obj.__module__

    return info

class MyClass:
  def __init__(self, name, age, student):
    self.name = name
    self.age = age
    self.student = student


  def say_hello(self):
    print(f"Hello, {self.name}!")


my_object = MyClass("Alice", 30, True)
my_object_info = introspection_info(my_object)
print(my_object_info)
