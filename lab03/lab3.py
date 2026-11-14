print('-----------------------------')
print('Задание 1')
lst = [1, 2, 3, 4, 5, 6]
tpl = (1, 2, 3, 4, 5, 6)

print(type(lst), id(lst))
print(type(tpl), id(tpl))

print('id списка до изминения: ', id(lst))
lst[0] = 13
print('id списка после изминения: ', id(lst))

print('id старого кортежа: ', id(tpl))
new_tpl = (1, 2, 3, 4, 5, 666)
print('id нового кортежа: ', id(new_tpl))

print('-----------------------------')
print('Задание 2')
names = [
    'Anna', 'Chris', 'William', 'Oliver', 'Anna', 'Ethan',
    'Olivia', 'Chris', 'Oliver', 'Chloe', 'Chloe', 'Chris'
]

print('Исходный список: ', names)
print('Количество элементов: ', len(names))

st_names = set(names)

print('Множество: ', st_names)
print('Количество элементов: ', len(st_names))

print('-----------------------------')
print('Задание 3')
import timeit

print('РАЗМЕР 1000')
lst_1 = list(range(1000))
st_1 = set(lst_1)
print('Список (эл-т есть): ', timeit.timeit('500 in lst_1', globals=globals(), number=1000))
print('Множество (эл-т есть): ', timeit.timeit('500 in st_1', globals=globals(), number=1000))
print('Список (эл-та нет): ', timeit.timeit('-666 in lst_1', globals=globals(), number=1000))
print('Множество (эл-та нет): ', timeit.timeit('-666 in st_1', globals=globals(), number=1000))

print('РАЗМЕР 10000')
lst_2 = list(range(10000))
st_2 = set(lst_2)
print('Список (эл-т есть): ', timeit.timeit('5000 in lst_2', globals=globals(), number=1000))
print('Множество (эл-т есть): ', timeit.timeit('5000 in st_2', globals=globals(), number=1000))
print('Список (эл-та нет): ', timeit.timeit('-666 in lst_2', globals=globals(), number=1000))
print('Множество (эл-та нет): ', timeit.timeit('-666 in st_2', globals=globals(), number=1000))

print('РАЗМЕР 100000')
lst_3 = list(range(100000))
st_3 = set(lst_3)
print('Список (эл-т есть): ', timeit.timeit('50000 in lst_3', globals=globals(), number=1000))
print('Множество (эл-т есть): ', timeit.timeit('50000 in st_3', globals=globals(), number=1000))
print('Список (эл-та нет): ', timeit.timeit('-666 in lst_3', globals=globals(), number=1000))
print('Множество (эл-та нет): ', timeit.timeit('-666 in st_3', globals=globals(), number=1000))

print('-----------------------------')
print('Задание 4')
import sys

books = {
    'A-10': 'Python для чайников', 'A-11': 'C++ для чайников',
    'A-12': 'Что-то для чайников', 'A-13': 'Чайники',
    'A-14': 'Чай', 'A-15': 'Ghbdtn — Что хотели написать?'
}
print('Книга под номером A-11: ', books['A-11'])

lst_books = ['Python для чайников', 'C++ для чайников', 'Что-то для чайников',
             'Чайники', 'Операционные системы', 'Ghbdtn — Что хотели написать']
tpl_books = tuple(lst_books)
st_books = set(lst_books)

print('Размер словаря: ', sys.getsizeof(books))
print('Размер списка: ', sys.getsizeof(lst_books))
print('Размер кортежа: ', sys.getsizeof(tpl_books))
print('Размер множества: ', sys.getsizeof(st_books))

print('-----------------------------')
print('Вариант 2')
rules = ('Техно', 21, 5)
app = [501, 507, 512, 526, 531, 544]
debts = {507, 526, 544}
books = {
    'B-101': 'Чистый код', 'B-102': 'Алгоритмы', 'B-103': 'Как использвать VPN',
    'B-104': 'Методичка по блокировкам', 'B-105': 'TARGET PECH FLAVOR'
}
print('Правила выдачи:', f'библиотека «{rules[0]}», {rules[1]} день, не более {rules[2]} книг')
print('Заявки в порядке поступления: ', ', '.join(map(str, app)))
print('Читатеи с задолжностью: ', ', '.join(map(str, debts)))
print('Книги: ')
for number, title in books.items():
    print(f'{number}: «{title}»')

app.append(558)
print('После добавленя заявки: ', ', '.join(map(str, app)))

hum = 526
has_debt = hum in debts
print(f'Читатель {hum} имеет задолжность: ', 'Да' if has_debt else 'Нет')

num = 'B-102'
book_title = books.get(num)
print(f'Книга с номером {num}: «{book_title}»')

print('-----------------------------')
