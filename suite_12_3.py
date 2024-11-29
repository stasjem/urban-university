'''
Практическое задание
2024/01/11 00:00|Домашнее задание по теме "Систематизация и пропуск тестов".
Цель: понять на практике как объединять тесты при помощи TestSuite. Научиться
пропускать тесты при помощи встроенных в unittest декораторов.

Задача "Заморозка кейсов":
Подготовка:
В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.
Часть 1. TestSuit.
Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
Создайте объект класса TextTestRunner, с аргументом verbosity=2.
'''

import unittest
import tests_12_2 as code



class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner("name1666")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner("name2")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)



    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner = Runner("name3")
        runner2 = Runner("name4666")
        for i in range(10):
            runner.run()
            runner2.walk()
        self.assertNotEqual(runner.distance, runner2.distance)


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
    all_results = {}
    is_frozen = True
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        test_tournament = Tournament(90, self.name1, self.name3)
        a = test_tournament.start()
        # print(a)
        self.all_results['Усейн и Ник'] = a
        key = max(a.keys())
        self.assertTrue(a[key] == self.name3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        test_tournament = Tournament(90,self.name2, self.name3)
        a = test_tournament.start()
        self.all_results['Андрей и Ник'] = a
        key = max(a.keys())
        self.assertTrue(a[key] == self.name3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        test_tournament = Tournament(90, self.name1, self.name2, self.name3)
        a = test_tournament.start()
        self.all_results['Усейн, Андрей и Ник'] = a
        key = max(a.keys())
        self.assertTrue(a[key] == self.name3)


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(code.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)

runner.run(suite)
