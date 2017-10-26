# Дан список чисел. Выведите значение наибольшего элемента в списке,
# а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.

sr = input()
if sr.find(", ") > 0:
    lists = list(sr.replace(", ", ""))
elif sr.find(",") > 0:
    lists = sr.split(",")
elif sr.find(" ") > 0:
    lists = sr.split(" ")
else:
    lists = list(sr)

maximum = max(lists)
index_max = lists.index(maximum)
print(maximum, index_max)
