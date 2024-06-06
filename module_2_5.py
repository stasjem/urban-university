'''
Задача "Матрица воплоти":
Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.

Пункты задачи:
Объявите функцию get_matrix и напишите в ней параметры n, m и value.
Создайте пустой список matrix внутри функции get_matrix.
Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
В первом цикле добавляйте пустой список в список matrix.
Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
Во втором цикле пополняйте ранее добавленный пустой список значениями value.
После всех циклов верните значение переменной matrix.
Выведите на экран(консоль) результат работы функции get_matix.

'''

def get_matrix(n, m, value):
    matrix = []
    for a in range(n):
        matrix.append([])
        for b in range(m):
            matrix[a].append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)







'''
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
'''

# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# students_s = sorted(students)
# print(students_s)
# numbers = [1, 2, 3, 4, 5]
# primes = []
# not_primes = []
#
# def is_prime(num):
#   """
#   Функция проверки простого числа.
#   """
#   if num <= 1:
#     return False
#   for i in range(2, int(num*0.5) + 1):
#     if num % i == 0:
#       return False
#   return True
#
# for number in numbers:
#
#   if is_prime(number):
#     primes.append(number)
#   elif number == 1:
#     continue
#   else:
#     not_primes.append(number)
#
# print(f"Простые числа: {primes}")
# print(f"Не простые числа: {not_primes}")