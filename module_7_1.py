'''
2023/11/12 00:00|Домашнее задание по теме "Режимы открытия файлов"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.

Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и
обладать следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке
разделены запятой с пробелами.

Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и
возвращает единую строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .

Пример результата выполнения программы:
Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

Вывод на консоль:
Первый запуск:
Spaghetti, 3.4, Groceries
Продукт Potato уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Второй запуск:
Spaghetti, 3.4, Groceries
Продукт Potato уже есть в магазине
Продукт Spaghetti уже есть в магазине
Продукт Potato уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Как выглядит файл после запусков:



Примечания:
Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
При проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
Не забывайте закрывать файл вызывая метод close() у объектов файла.

'''

from pprint import pprint
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")

class Product:
    name = '123' #название продукта (строка).
    weight = '1234' #общий вес товара (дробное число) (5.4, 52.8 и т.п.).
    category = '12345' #категория товара (строка).

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category


       #  file = open('products.txt', 'r')
       # # file.read(f'{self.name}, {self, weight}, {self.category}')
       #  file.read()
       #  file.close()
        # pprint('1')
        # pprint(file.read())
        # pprint('2')
        #
        # file = open('products.txt', 'a')
        # file.write(f'{self.name}, {self,weight}, {self.category}')
        # file.close()
    # self.__st

    def __str__(self):
        # self.name = name
        # self.weight = weight
        # self.category = category
        print('123445')
        print(f'{self.name},{self.weight},{self.category}')
        return f'{self.name},{self.weight},{self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        logging.info("An INFO")
    # def __init__(self, name, weight, category):
    #     self.name = name
    #     self.weight = weight
    #     self.category = category
    #     file = open('products.txt', 'a')
    #     file.write(f'{self.name}, {self,weight}, {self.category}')
    #     file.close()

    def get_products(self):
        with open(self.__file_name,'r')  as file:
            products = file.read()
            print(products)
            pprint(products)

        # file = open(self.__file_name, 'r')
        # file.read()
        # file.close()

    def add(self, *products):
        set_products=self.get_products()
        with open(self.__file_name, 'a') as file:
            products in products

        # file = open(self.__file_name, 'a')
        # file.write(f'{self.name},{self.weight},{self.category}')
        # file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())