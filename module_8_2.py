'''
2023/11/25 00:00|Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции".
Цель: понять как работают исключения внутри функций и как обрабатываются эти исключения на практике
при помощи try-except.

Задача "План перехват":
Напишите 2 функции:
Функция personal_sum(numbers):
Должна принимать коллекцию numbers.
Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError,
увеличив счётчик incorrect_data на 1.
В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во
некорректных данных.
Функция calculate_average(numbers)
Среднее арифметическое - сумма всех данных делённая на их количество.
Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
Также в numbers может быть записана не коллекция, а другие типы данных, например числа. Обработайте исключение
TypeError выводя строку 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None.

Пункты задачи:
Создайте функцию personal_sum на основе условий задачи.
Создайте функцию calculate_average на основе условий задачи.
Вызовите функцию calculate_average несколько раз, передав в неё данные разных вариаций.
Пример результата выполнения программы:
Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

Вывод на консоль:
Некорректный тип данных для подсчёта суммы - 1
Некорректный тип данных для подсчёта суммы - ,
Некорректный тип данных для подсчёта суммы -
Некорректный тип данных для подсчёта суммы - 2
Некорректный тип данных для подсчёта суммы - ,
Некорректный тип данных для подсчёта суммы -
Некорректный тип данных для подсчёта суммы - 3
Результат 1: 0
Некорректный тип данных для подсчёта суммы - Строка
Некорректный тип данных для подсчёта суммы - Ещё Строка
Результат 2: 2.0
В numbers записан некорректный тип данных
Результат 3: None
Результат 4: 26.5
'''
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("")
logging.info("")
logging.info("")

def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for value in numbers:
            if isinstance(value, int):
                result += int(value)
            else:
                try:
                    print(f"Некорректный тип данных для подсчёта суммы - {value}")
                    logging.info(f"Некорректный тип данных для подсчёта суммы - {value}")
                except TypeError:
                    incorrect_data += 1
                    logging.info(f"--------str 99--------{incorrect_data}")

    logging.info([result, incorrect_data])
    logging.info(f"result {[result, incorrect_data]}")
    return [result, incorrect_data]


def calculate_average(numbers):
    logging.info(f"--------------------{type(numbers)}-----------------------")
    print(f"{type(numbers)}")

    if isinstance(numbers, str):
        try:
            personal_sum(numbers)
        except TypeError:
            print(f"В numbers записан некорректный тип данных.")


    if isinstance(numbers, list):
        logging.info(f"--------------------{type(numbers)}-----------------------")
        logging.info(f"--------------------{numbers}-----------------------")
        result_person = personal_sum(numbers)
        correct_num = len(numbers) - result_person[1]
        avg = result_person[0] / correct_num
        logging.info(f"--------------------{avg}-----------------------")

        for value_one in numbers:
            logging.info(f"--------------------{value_one}-----------------------")

        try:
            print(f"--------------------{type(result_person)}-----------------------")
            return avg

        except ZeroDivisionError:
            print("0")








    if isinstance(numbers, int):
        try:
            logging.info("-------------------------------------------")
        except TypeError:
            print(f"В numbers записан некорректный тип данных.")




print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
