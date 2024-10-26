from random import randint
from time import sleep
from threading import Thread, Event
from queue import Queue



class Table():

    def __init__(self, number, quest=None):
        self.number = number
        self.guest = quest


class Guest(Thread):

    def __init__(self, name, *args, **kwargs):
        super(Guest, self).__init__(*args, **kwargs)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe():
    def __init__(self, queue, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            found_table = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    found_table = True
                    break
            if not found_table:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")


    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for i in range(len(self.tables)):
                if self.tables[i].guest and not self.tables[i].guest.is_alive():
                    print(f"{self.tables[i].guest.name} покушал(-а) и ушёл(ушла). Стол номер {self.tables[i].number} свободен")
                    self.tables[i].guest = None
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        self.tables[i].guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables[i].number}")





# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
