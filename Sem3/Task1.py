#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

lst = []
sum = 0

for i in range(randint(4,10)):
    lst.append(randint(1,15))
print(lst)

for i in range(len(lst)):
    if i %2  != 0:
        sum += lst[i]
print(sum)
