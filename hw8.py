# hw_8.1.
# Додати 1 до числа
# Ваше завдання — написати функцію add_one, яка приймає список із цифр, які у свою чергу є одним числом.
# До нього необхідно додати 1.
# Тобто. Вам необхідно з набору цифр, що входять до списку, отримати число,
# скласти його з 1 і отриману суму, знову розбити на список із цифр.
# В результаті функція повертає список із цифр, що становлять значення суми.
# Так зі списку з цифрами [1, 2, 3, 4], має вийти число 1234. До нього додаємо 1, і отримуємо 1235.
# Після цього потрібно розбити отримане число на складові цифри.
# У результаті має бути список [1, 2, 3, 5], який повертає функція.
# Якщо ви хочете себе перевірити, використайте цей unit test
# def add_one(some_list):
#     pass
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")
# def add_one(some_list):
#     i = 0
#     nstr = ''
#     for let in some_list:
#         if let !=',' and let !=' ':
#             nstr = nstr + str(let)
#             i += 1
#     nstr = int(nstr) + 1
#     lnstr = [int(x) for x in str(nstr)]
#     return lnstr
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")

# hw_8.2
#  Паліандром
# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво
# без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False
# Приклад:
# def is_palindrome(text):
#     pass
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")
# def is_palindrome(text):
#     ntext = ''.join(let.lower() for let in text if let.isalnum())
#     ntext_2 = ntext[::-1]
#     return ntext == ntext_2
#
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")


# hw_8.3
# Унікальне число
# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел, знаходить серед них унікальне число та
# повертати його. Унікальне число - це число, яке зустрічається в списку один раз.
# Випадок, коли в одному списку буде кілька унікальних чисел, перевіряти не потрібно.
# Приклад:
# def find_unique_value(some_list):
#    pass
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")

def find_unique_value(some_list):
   unique = int
   for number in some_list:
      if some_list.count(number) == 1:
         unique = number

   return unique

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")