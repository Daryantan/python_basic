# hw_9.1
# Визначити популярність певних слів у тексті
# На вхід функції popular_words передаються два аргументи. Текст та список слів, популярність яких необхідно визначити.
# При вирішенні цього завдання зверніть увагу на такі моменти
# Слова необхідно шукати у всіх регістрах. Тобто. якщо необхідно знайти слово "one",
# значить для нього будуть підходити слова "one", "One", "oNe", "ONE" і т.д.
# Шукані слова завжди вказані в нижньому регістрі
# Якщо слово не знайдено жодного разу, його необхідно повернути у словнику зі значенням 0 (нуль)
# Вхідні параметри: Текст і масив слів, що шукаються.
# Вихідні параметри: Словник, у якому ключами є шукані слова та значеннями,
# скільки разів кожнє слово зустрічаються у орігінальному тексті.
# Приклад:
#
# def popular_words (text, words):
# pass
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1' print('OK')
#

# def popular_words (text, words):
#     text_lower = text.lower().split()
#     wrds = {}
#     '''
#     створюємо словник, щоб зберігати у нього результат, після чого в циклі підраховуємо кількість слів
#     '''
#     for word in words:
#         wrds[word] = text_lower.count(word)
#     return wrds
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')



# hw_9.2
# Різниця між числами
# Є набір чисел (float або int). Вам потрібно знайти різницю між найбільшим (максимум) і найменшим (мінімум) елементом.
# Ваша функція difference має вміти працювати з невизначеною кількістю аргументів.
# Якщо аргументів немає, то функція повертає 0 (нуль).
# Якщо з 3-м тестом будуть проблеми, використовуйте функцію округлення round(x, 2),
# де х це число, яке потрібно округлити.
# Вх. Дані: Змінна кількість аргументів як числа (int, float).
# Вих. Дані: Різниця між максимумом і мінімумом як число (int, float).
# Приклади:
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')

def difference(*args):
    if not args:
        return 0
    res = round(max(args) - min(args), 2)
    return res

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
