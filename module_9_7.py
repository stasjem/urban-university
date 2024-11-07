'''
Практическое задание
2023/12/05 00:00|Домашнее задание по теме "Декораторы"
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11

Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three

Файл module_9_7.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!
'''
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1:
            for i in range(2, int(result*0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    return result
            print("Простое")
            return result
        else:
            print("Составное")
            return result
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
result = sum_three(5, 2, 8)
print(result)