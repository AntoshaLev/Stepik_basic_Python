"""Задача 1"""

# a = int(input())
# b = int(input())
# c = int(input())
# p = ((a + b + c) / 2)
# print((p*(p-a)*(p-b)*(p-c))**0.5)

"""Задача 2"""

# a = int(input())
# if -15 <= a < 12 or 14 < a < 17 or 19 <= a < float("+inf"):
#     print(True)
# else:
#     print(False)


"""Задача 3"""

# A = float(input())
# B = float(input())
# C = input()
#
# if C == '+':
#     print(A + B)
# elif C == '-':
#     print(A - B)
# elif C == '*':
#     print(A * B)
# elif C == '/':
#     if B != 0:
#         print(A / B)
#     else:
#         print("Деление на 0!")
# elif C == 'mod':
#     if B != 0:
#         print(A % B)
#     else:
#         print("Деление на 0!")
# elif C == 'pow':
#     print(A ** B)
# elif C == 'div':
#     if B != 0:
#         print(A // B)
#     else:
#         print("Деление на 0!")


"""Задача 4"""

# A = input()
# if A == "треугольник":
#     a = float(input())
#     b = float(input())
#     c = float(input())
#     p = ((a + b + c) / 2)
#     print((p*(p-a)*(p-b)*(p-c))**0.5)
# elif A == "прямоугольник":
#     a = float(input())
#     b = float(input())
#     print(a * b)
# elif A == "круг":
#     r = float(input())
#     print(3.14 * (r ** 2))

"""Задача 5"""

# A, B, C = (int(input()), int(input()), int(input()))
# if A >= B >= C:
#     print(A, C, B, sep='\n')
# elif A >= C >= B:
#     print(A, B, C, sep='\n')
# elif B >= A >= C:
#     print(B, C, A, sep='\n')
# elif B >= C >= A:
#     print(B, A, C, sep='\n')
# elif C >= A >= B:
#     print(C, B, A, sep='\n')
# elif C >= B >= A:
#     print(C, A, B, sep='\n')

"""Задача 6"""

n = int(input())
s = str(n)
ls = s[len(s)-1]
if ls == 1 or n == 1:
    print(n, "программист")
elif 2 <= n <= 4 or ls == 2 or ls == 3 or ls == 4:
    print(n, "программиста")
elif n == 5 or n == 6 or n == 7 or n == 8 or n == 9 or s == 5 or s == 6 or s == 7 or s == 8 or s == 9:
    print(n, "программистов")



