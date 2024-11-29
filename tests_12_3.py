'''
Часть 2. Пропуск тестов.
Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который
при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и
выводить сообщение 'Тесты в этом кейсе заморожены'.
Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
Пример результата выполнения тестов:
Вывод на консоль:
test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
test_run (tests_12_3.RunnerTest.test_run) ... ok
test_walk (tests_12_3.RunnerTest.test_walk) ... ok
test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'
test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'
test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'
----------------------------------------------------------------------
Ran 6 tests in 0.000s OK (skipped=3)

Файлы suite_12_3.py и tests_12_3.py, где произошли изменения загрузите на ваш GitHub репозиторий.
В решении пришлите ссылку на него.
Успехов!

'''
import tests_12_1 as code
import suite_12_3 as suite
import unittest

testST = unittest.TestSuite()
# testST.addTest(unittest.makeSuite(suite.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(code.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(suite.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)
