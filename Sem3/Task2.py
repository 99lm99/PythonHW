# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

lenght = int(input("Введите длину списка: "))
lst = []
lst2 = []

for i in range(lenght):
    lst.append(randint(1, 95))
print(f"Список чисел: {lst}")

if lenght % 2 == 0:
    for i in range(int(lenght / 2)):
        lst2.append(lst[i] * lst[-i - 1])
else:
    for i in range(int(lenght  / 2 + 1)):
        lst2.append(lst[i] * lst[-i - 1])

print(f"Произведение пар чисел  {lst2}")
