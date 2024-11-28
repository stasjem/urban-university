'''
Практическое задание
2024/01/09 00:00|Домашнее задание по теме "Методы Юнит-тестирования"
Цель: освоить методы, которые содержит класс TestCase.

Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция,
которую нужно пробежать и список участников. Также присутствует метод start,
который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который
будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на
дистанцию 90. У объекта класса Tournament запускается метод start, который возвращает
словарь в переменную all_results. В конце вызывается метод assertTrue, в котором
сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.

Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка.
В результате его работы бегун с меньшей скоростью может пробежать некоторые
дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.
Пример результата выполнения тестов:
Вывод на консоль:
{1: Усэйн, 2: Ник}
{1: Андрей, 2: Ник}
{1: Андрей, 2: Усэйн, 3: Ник}

Ran 3 tests in 0.001s
OK

Примечания:
Ваш код может отличаться от строгой последовательности описанной в задании.
Главное - схожая логика работы тестов и наличие всех перечисленных переопределённых методов из класса TestCase.
Файл tests_12_2.py c классами тестов загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!
'''

import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return {i + 1: finishers[place] for i, place in enumerate(sorted(finishers.keys()))}


class TournamentTest(unittest.TestCase):
    # all_results = {}
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.name1 = Runner('Усэйн', 10)
        self.name2 = Runner('Андрей', 9)
        self.name3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            # print(cls.all_results)
            print(key)
            for i in cls.all_results[key]:
                # print(i)
                print(f'{cls.all_results[key][i]} - {i}')
            print()


    def test_run_1(self):
        test_tournament = Tournament(90, self.name1, self.name3)
        a = test_tournament.start()
        # print(a)
        self.all_results['Усейн и Ник'] = a
        key = max(a.keys())
        self.assertTrue(a[key] == self.name3)

    def test_run_2(self):
        test_tournament = Tournament(90,self.name2, self.name3)
        a = test_tournament.start()
        self.all_results['Андрей и Ник'] = a
        key = max(a.keys())
        self.assertTrue(a[key] == self.name3)

    def test_run_3(self):
        test_tournament = Tournament(90, self.name1, self.name2, self.name3)
        a = test_tournament.start()
        self.all_results['Усейн, Андрей и Ник'] = a
        key = max(a.keys())
        self.assertTrue(a[key] == self.name3)


if __name__ == '__main__':
    unittest.main()
