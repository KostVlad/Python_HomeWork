# Дан список чисел. Выведите значение наибольшего элемента в списке,
# а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.

lists = (input()).split()
maximum = max(lists)
index_max =lists.index(maximum)
print(maximum, index_max)