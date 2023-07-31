# A = int(input())
# B = int(input())
# H = int(input())
# if A <= H <= B:
#     print("Это нормально")
# elif H < A:
#     print("Недосып")
# else:
#     print("Пересып")


# A = int(input())
# if not 1900 <= A <= 3000:
#     print("Введите корректное число")
#     if A / 400 or not A / 100:
#         print("Обычный")
#     elif A / 4:
#         print("Весокосный")
#     else:
#         print("Обычный")
# else:
#     A = int(input())
#     if not 1900 <= A <= 3000:
#         print("Вы не справились(")
#         if A / 400 or not A / 100:
#             print("Обычный")
#         elif A / 4:
#             print("Весокосный")
#         else:
#             print("Обычный")


A = int(input())
if A % 4 == 0 and (not A % 100 == 0 or A % 400 == 0):
    print("Високосный")
else:
    print("Обычный")