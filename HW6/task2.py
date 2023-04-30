"""Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)"""

import random
arr = [random.randint(1, 100) for _ in range(0,20)]
print(arr)
min = int(input("Введите минимальное значение:"))
max = int(input("Введите максимальное значение:"))
for i in range(len(arr)):
    if min <= arr[i] <= max:
        print(i ," ", end = '')