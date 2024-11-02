'''
2023/12/22 00:00|Домашнее задание по теме "Обзор сторонних библиотек Python"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.
Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.

Задача:
Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и
 функциями. К каждой библиотеке дана ссылка на документацию ниже.
Если вы выбрали:
requests - запросить данные с сайта и вывести их в консоль.
pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в
 консоль.
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная
библиотека и как вы расширили возможности Python с её помощью.
Примечания:
Можете выбрать не более 3-х библиотек для изучения.
Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.
'''



import requests
import numpy
from PIL import Image, ImageFilter

r = requests.get('https://google.com')
print(r.status_code)
print(r.headers['content-type'])
print(r.cookies)
print(r.content)
print()

a = numpy.array([[1, 2, 3], [4, 5, 6]])
print(numpy.random.sample(3))
print(a.sum())
print(a.min())
print(a.max())


img = Image.open("Cat03.jpg")
print(img.size)
img = img.filter(ImageFilter.CONTOUR)

img = img.resize((200, 200))
img.save("Cat04" + ".png")
img.show()
