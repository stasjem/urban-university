'''
Практическое задание
2024/01/12 00:00|Домашнее задание по теме "Логирование"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.
Цель: получить опыт использования простейшего логирования совместно с тестами.

Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub.
(Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и
если передано отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на
следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация:
уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен
успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его
на уровне WARNING с сообщением "Неверная скорость для Runner".
test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и
логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
Пример результата выполнения программы:
Пример полученного файла логов runner_tests.log:


Файл tests_12_4.py с классами тестов и runner_tests.log с
логами тестов загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!
'''

import unittest
# import tests_12_1 as code
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("")
logging.info("")
logging.info("")

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
        try:
            runner = Runner("name1666")
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner("name2")
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип имени для Runner', exc_info=True)

if __name__ == "__main__":
    unittest.main()
