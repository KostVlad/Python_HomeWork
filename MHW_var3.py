#Дан файл с каким-то математическим выражением, которое содержит скобки разных типов “{[()]}” в любом порядке. Проверить сбалансированны ли #скобки. В случае сбалансированности вывести результат вычисления выражения, иначе вывести сообщение об ошибке.

import sys

brackets = "()[]{}"
operation = "+-*/%"
open_brackets = []


def replacing():
    with open("file.txt", "r") as ff:
        equation = ff.read()
        equation = equation.replace("{", "(")
        equation = equation.replace("}", ")")
        equation = equation.replace("[", "(")
        equation = equation.replace("]", ")")
        try:
            result = eval(equation)
            print(equation, "=", result)
        except SyntaxError:
            print(equation)
            print("Не правильная синтаксическая конструкция, "
                  "проверьте правильность растановки знаков мат операций и попробуйте снова")


f = open("file.txt", "r")
for char in f.read():
    index = brackets.find(char)  # если элемент-скобка, то вернет номер первого вхождения, если нет -1
    if index >= 0:  # Является ли элемент скобкой?
        if index % 2 == 0:  # если номер элемента четный => открыв. скобка
            open_brackets.append(char)  # Добавляем элемент в конец списка
        else:
            if not open_brackets:  # Проверка, список пустой?
                print("Ошибка! Не парная закрывающаяся скобка", char)
                sys.exit()
            else:
                last_brackets = open_brackets.pop()  # Удаление и возвращ. последнего элем. списка
                test = last_brackets + char  # Последний элемент склеиваем со считанной скобкой
                if brackets.find(test) < 0:  # Поиск склеиных скобок
                    print("Ошибка! Не парные скобки, порядок нарушен", test)
                    sys.exit()
    else:  # Работа с символами, отличными от скобок
        number = operation.find(char)
        if number < 0:  # Если считанные символ не явл. символом мат. операции
            try:
                CharNum = int(char)  # Проверка является ли символ числом
            except ValueError:
                print("Ошибка! В выражении не известное значение: \"",
                      char, "\" используйте числа, скобки, или символы мат операций!")
                sys.exit()

f.close()
if not open_brackets:
    print("Операция валидации скобок завершена")
    replacing()
else:
    if len(open_brackets) > 1:  # Если в списке еще остались какие-то скобки
        print("Ошибка! Есть не закрытые скобки", open_brackets)
    else:
        print("Ошибка! Есть не закрытая скобка", open_brackets)
