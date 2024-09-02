'''
2023/11/17 00:00|Домашнее задание по теме "Оператор "with".
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.

Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

for name, words in get_all_words().items():
  # Логика методов find или count
'''

class WordsFinder:
    def __init__(self,*file_names):
        self.file_names=file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name,'r',encoding='utf-8') as file:
                    content=file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content=content.replace(punct,'')
                    words = content.split()
                    all_words[file_name] = words

            except FileNotFoundError:
                print(f"файл {file_name} не найден")


        return all_words

    def find(self, word):
        word = word.lower()
        resu = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                resu[file_name] = words.index(word)
            else:
                resu[file_name] = -1

        return resu

    def count(self, word):
        word = word.lower()
        resu = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            resu[file_name] = words.count(word)
        return resu






finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
