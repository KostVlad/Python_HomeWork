# Написать консольную утилиту, передав которому путь к какой то папке,
# она выводит список файлов и папок, которые есть в этой папке.
# Используя библиотеки os и sys

import os
print("Введите путь к папке")
s = input()
q = os.listdir(s)
print(q)
