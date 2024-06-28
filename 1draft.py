'''
module2hard.py

Пример кратности(деления без остатка):
1 + 2 = 3 (сумма пары)
9 / 3 = 3 (ровно 3 без остатка)
9 кратно 3 (9 делится на 3 без остатка)
'''
import random

a = random.randint(3, 20)
print(a)

#b = random.randint(3, 20)
#c = ''
def any_lvl(a):
    print(a%2)
    if a%2==0:
        print(a)
        return a
    else:
        print("Нету")


c = any_lvl(a)

print(range(c, 20))
# print(a)
# print(b)
# print(a + b)
# print(a/(a + b))
