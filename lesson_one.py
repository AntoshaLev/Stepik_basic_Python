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

Вывод:
input() - с клавиатуры
open() - из файла

Логические операторы:
and - и
or - или
not - не


if_else:
if - если
elif - иначе если
else - иначе/в противном случае

типы:
list - список

Циклы:

WHILE

a = 0
my_list = [12, 'qwerty', 42]
while a < len(my_list)  -  пока а меньше количества элементов в списке будем выполнять -->
a + 1
print(a) - столько элементов в списке

FOR IN

my_list = [12, 'qwerty', 42]
for i in my_list пройди по каждому элементу из списка
print(i)  Выведет каждое значение списка в новой строке

CONTINUE

for i in range(10)
    if i == 5
        continue -- бросай все что делал и иди дальше
    print(i) запринтится без 5

BREAK

for i in range(10)
    if i == 5
        break -- заверши цикл на этом
    print(i) до 4

enumerate
my_list = [1, 2, 3, 4, 5, 6]
for i, number in enumerate(my_list, start = 1) пронумеруй каждое значение из списка (нумерацию начни с числа 1)
print(i, numbers)
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
