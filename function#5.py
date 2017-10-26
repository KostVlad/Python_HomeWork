# Написать функцию avaranger, которая принимает 1 аргумент -
# любое число и возвращается среднее арифметическое значение,
# на основании текущего числа и предыдущих, которые были введены ранее.
# Например
# >>> avaranger(10) Среднее арифметическое 10
# >>> 10
# >>> avaranger(11) Среднее арифметическое 10 и 11
# >>> 10.5
# >>> avaranger(12) Среднее арифметическое 10, 11 и 12
# >>> 11
lists_num = []

def avaranger(numbr):
    lists_num.append(numbr)  # Вставляем элемент в конец списка
    middle = sum(lists_num) / len(lists_num)
    print(middle)
    inp()

def inp():
    try:
        num = float(input())
    except ValueError:
        print("Введите число")
        inp()

    avaranger(num)
# Конец функции
inp()






