# hw_3.1
# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма,
# виходячи з дії, обчислює та друкує результат.
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!
# print("Please, enter first number: ")
# a = int(input())
# print("Please, enter second number: ")
# b = int(input())
# print("Please, enter number of action : ")
# print(" 1) Addition \n 2) Deletion \n 3) Multiplication \n 4) Division")
# action = int(input())
# match action:
#     case 1:
#         print(a+b)
#     case 2:
#         print(a-b)
#     case 3:
#         print(a*b)
#     case 4:
#         if b == 0:
#             print("Ouups! Division by zero is impossible!")
#         else:
#             print(a/b)
#     case _:
#         print("Invalid option, please, try again")


# hw_3.2
# Перемістити елемент у списку
# Ваша програма має перенести останній елемент списку з кінця на початок, тобто, останній елемент списку має стати першим.
# Послідовність інших елементів не має змінюватися.
# Порожній список або список з одним елементом повинен залишитися незмінним.
# Кількість елементів у списку може бути будь-яким – нуль та більше!
# Приклади:
# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10
# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.

# arr = [12, 3, 4, 10]
# arr = [1]
# arr = []
# arr = [12, 3, 4, 10, 8]

# if len(arr) == 0:
#     print(arr)
# else:
#     arr.insert(0, arr[-1])
#     arr.pop()
#     print(arr)


# hw_3.3
# Розділити один список на два списки
#
# Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
# Тобто, в результаті повинен вийти список із 2-х списків.
# Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
# Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.
# Важливо! Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
# у списку парна кількість елементів і в списку непарна кількість елементів.
# Приклади:
# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]
# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.

arr = [1, 2, 3, 4, 5, 6]
# arr = [1, 2, 3]
# arr = [1, 2, 3, 4, 5]
# arr = [1]
# arr = []
if len(arr) % 2 == 0:
    ar1 = arr[:len(arr) // 2]
    ar2 = arr[len(arr) // 2:]
    res = [ar1, ar2]
elif len(arr) == 0 or len(arr) == 1:
    res = [arr, arr]
elif len(arr) % 2 != 0:
    ar1 = arr[:(len(arr)//2)+1]
    ar2 = [arr[1+len(arr) // 2:]]
    res = [ar1, ar2]
print(res)



