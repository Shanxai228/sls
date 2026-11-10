#Модуль ввода комплексных чисел 
for i in range(4):
    numbers = int(input("Введите число"))
    print ("numbers")

#Модуль арифметики
import math
a = int(input("Введите комплексное число"))
b = int(input("Введите комплексное число"))
j = 1
z = a + b * j
print(a + b)  
print(a - b)
print(a / b)  
print(a * b)

#Модуль вывода — вывод результата в алгебраической и тригонометрической форме
def print_complex(a: float, b: float):
    # Расчет модуля (r) и аргумента (phi)
    modulus = math.sqrt(a**2 + b**2)
    argument = math.atan2(b, a)
    # Формирование алгебраической формы (a + bi)
    sign = "+" if b >= 0 else "-"
    algebraic = f"{a} {sign} {abs(b)}i"
    # Формирование тригонометрической формы
    trigonometric = f"{modulus:.4f} * (cos({argument:.4f}) + i*sin({argument:.4f}))"
    # Вывод результатов в консоль
    print("Алгебраическая форма:      ", algebraic)
    print("Тригонометрическая форма:  ", trigonometric)
    print(f"Модуль r = {modulus:.4f}, аргумент ф = {argument:.4f} рад "
          f"({math.degrees(argument):.2f}°)")
# 1. Запрашиваем у пользователя действительную и мнимую части
real_part = float(input("Введите действительную часть (a): "))
imag_part = float(input("Введите мнимую часть (b): "))
# 2. Передаем переменные напрямую в функцию вывода
print_complex(real_part, imag_part)



