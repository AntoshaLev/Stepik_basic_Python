"""
Оператор	Значение	            Пример
+	        добавление	            4 + 5
—	        вычитание	            8 — 3
*	        умножение	            5 * 5
/	        деление	                4 / 2
%	        остаток от деления	    7 % 2
**	        возведение в степень	2 ** 3
//	        целочисленное деление	15 // 4
e           экспоненциальная запись(10)          10е2 10*10 во 2 степени
"""

print(1.2345e3)  # 1234.5

print(1.2345e-3)  # 0.0012345 2014.0

print(2014.0 ** 14)  # 1.806477376560755e+46  7/3

print(7 / 3)  # 2.3333333333333335

print(7 // 3)  # 2

x = int(2.66)
print(x)  # 2 -1.6

y = int(-1.6)
print(y)  # -1

print(9 ** 19 - int(float(9 ** 19)))  # 89

# Определение типа

print(type(7))  # <class 'int'>

print(type(7.6))  # <class 'float'>

user_one = int(input("Введите число: "))
user_two = float(input("Введите число: "))

one_and_two = user_two + user_one

print(one_and_two)


X = int(input("Сколько часов вы спите ночью: "))
Y = int(input("Сколько минут вы спите днем: "))
print(X*60 + Y)

X = int(input())
print(int(X / 60))
print(X % 60)

X = int(input())
H = int(input())
M = int(input())
T = int(X + (H * 60) + M)
print(T // 60)
print(T % 60)
