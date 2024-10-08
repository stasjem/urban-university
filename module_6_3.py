'''
2023/11/06 00:00|Домашнее задание по теме "Множественное наследование"

Цель: закрепить знания множественного наследования в Python.

Задача "Мифическое наследование":
Необходимо написать 3 класса:
Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
x_distance = 0 - пройденный путь.
sound = 'Frrr' - звук, который издаёт лошадь.
И методами:
run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
y_distance = 0 - высота полёта
sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
И методами:
fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
Также обладает методами:
move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly
 соответственно.
get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
voice - который печатает значение унаследованного атрибута sound.
Пункты задачи:
Создайте классы родители: Horse и Eagle с методами из описания.
Создайте класс наследник Pegasus с методами из описания.
Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.

Пример результата выполнения программы:
Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

Вывод на консоль:
(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat

Примечания:
Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном наследовании:
 при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
Заметьте, что Pegasus издаёт звук "I train, eat, sleep, and repeat", т.к. по порядку сначала идёт наследование
 от Horse, а после от Eagle.

'''

class Horse:
    x_distance = 0 #- пройденный путь.
    sound = 'Frrr' #- звук, который издаёт лошадь.

    def __init__(self, dx):
        self.dx = dx

    def run(self, dx): #, где dx - изменение дистанции, увеличивает x_distance на dx.
        self.x_distance += dx


class Eagle:
    y_distance = 0 #- высота полёта
    sound = 'I train, eat, sleep, and repeat' #- звук, который издаёт орёл(отсылка)

    def __init__(self, dy):
        self.dy = dy

    def fly(self, dy): # где dy - изменение дистанции, увеличивает y_distance на dy.
        self.dy = dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self, dx=0, dy=0):
        Eagle.__init__(self, dy)
        Horse.__init__(self, dx)

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)


    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(f"{Eagle.sound}, {Horse.sound}")



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()


'''
(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat
'''