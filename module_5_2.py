'''
2023/10/27 00:00|Домашняя работа по уроку "Специальные методы классов"
Домашнее задание по уроку "Специальные методы классов"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новый класс House
Создайте инициализатор для класса House, который будет задавать
атрибут этажности self.numberOfFloors = 0
Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors
на параметр floors и выводить в консоль numberOfFloors
Полученный код напишите в ответ к домашнему заданию
'''



class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"Количество этажей изменено на: {self.numberOfFloors}")

my_house = House()
print(f"Начальное количество этажей: {my_house.numberOfFloors}")

my_house.setNewNumberOfFloors(5)
my_house.setNewNumberOfFloors(9)