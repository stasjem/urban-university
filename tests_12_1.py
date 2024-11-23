'''
Практическое задание
2024/01/08 00:00|Домашнее задание по теме "Простые Юнит-Тесты"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.
Цель: приобрести навык создания простейших Юнит-тестов

Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

Пункты задачи:
Скачайте исходный код для тестов.
Создайте класс RunnerTest и соответствующие описанию методы.
Запустите RunnerTest и убедитесь в правильности результатов.
Пример результата выполнения программы:
Вывод на консоль:
Ran 3 tests in 0.001s OK

Примечания:
Попробуйте поменять значения в одном из тестов, результаты
Файл tests_12_1.py с классом тестов загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!
'''


import unittest


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
    def test_walk(self):
        runner = Runner("name1666")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    def test_run(self):
        runner = Runner("name2")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    def test_challenge(self):
        runner = Runner("name3")
        runner2 = Runner("name4666")
        for i in range(10):
            runner.run()
            runner2.walk()
        self.assertNotEqual(runner.distance, runner2.distance)
