#Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:- Для n = 5: сумма = 11,55
number = int(input('Введите число: '))
i = 1
sum = 0
lst = []

for i in range(1, number + 1):
    x = (1 + (1/i)) ** i
    lst.append(x)
    sum+= x
print(lst)
print(round(sum, 2))
