# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# user_number = float(input("Введите число: "))

k = 1
p = 0
for k in range(1, 1000000):
    p = p + 4 * ((-1)**(k + 1)) / (2 * k - 1)


user_number = 100
pi = 3.1415936535907742
a = 3 + (int((p - 3) * from_user) / from_user)
print(a)
