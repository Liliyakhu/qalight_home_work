
# 1
# Дана строка. Определить является ли количество символов четным.
# s = 'Nisl scelerisque justo per hac cras purus lectus maecenas litora facilisi potenti.'
# ...
# > True or False
print('====== 1 task =======')

s = 'Nisl scelerisque justo per hac cras purus lectus maecenas litora facilisi potenti.'
# print(len(s))
if len(s) % 2 == 0:
    print('True')
else:
    print('False')

# 2
# Сформировать строку из 10 символов. На четных позициях должны находится четные цифры, на нечетных позициях - буквы.
# Пример корректных результатов
# '0a2b4c6d8e', '0a0a0a0a0a'
print('====== 2 task =======')
# для второго варианта из примера целесообразно:
c = '0a' * 5
print(c)

# для первого варианта:
a = '02468'
b = 'abcdefghijklmnopqrstuvwxyz'
d = list(a)
e = list(b)
p = []
for i in range(0, int(10/2)):
    o = d[i] + e[i]
    # print(o)
    p.append(o)
    # print(p)
t = ''.join(p)
print(t)

# 3
# Дана строка. Показать порядковый номер символов, совпадающих с последним символом строки.
print('====== 3 task =======')
s = 'Nisl scelerisque justo per hac cras purus lectus maecenas litora facilisi potenti'
# 2, 12, 58, 67, 69, 71, 78

# print(s[0])
# m = len(s)
# print(m)

# x = s[-1:]
# print(x)

li = []
while 'i' in s:
    h = s.rfind('i')
    # print(h + 1)
    li.append(str(h + 1))
    s = s[:h]
    # print(s)

# print(li)
v = ', '.join(reversed(li))
print(v)

# 4
# Дана строка. Определите, какой символ в ней встречается
# раньше: 'x' или 'w'. Если какого-то из символов нет,
# вывести сообщение об этом.
# нужно использовать конструкцию ветвления if-elif-else
print('====== 4 task =======')
s = 'jhkjkoiwejkh kjahlskdjfh  qwkjhlk zkjh kjhaswdefxkjh jkjhkjh'

k = s.find('x')
li = s.find('w')
# print('In \'',s,'\'')
print('In \'%s\'' % s)

if k > li:
    print('\'w\' is the first, not \'x\'')
elif k < li:
    print('\'x\' is the first, not \'w\'')
else:
    print('There is no \'x\' or \'w\' in the string.')


# 5
# Дана строка. Если ее длина больше 10, то оставить в строке
# только первые 6 символов, иначе дополнить строку символами
# 'o' до длины 12.
print('====== 5 task =======')
s = 'I love singing!'
if len(s) > 10:
    s = s[:6]
else:
    s = s + 'o' * (12-len(s))

print(s)

# 6
# Дана строка. Посчитать количество слов строке.
print('====== 6 task =======')
s = 'Nisl scelerisque justo per hac ras purus lectus maecenas litora facilisi potenti'
d = s.split()
print(len(d))
# Ліля, а якщо слова будуть розділені дваома пробілами як воно працюватиме?
# так само

# 7
# Дана строка. Заменить каждый четный символ или на 'a',
# если символ не равен 'a' или 'b', или на 'c' в противном случае.
print('====== 7 task =======')
s = 'abra cadabra'  # Nisl scelerisque justo per hac ras purus lectus maecenas litora facilisi potenti'

# print(len(s))
# d = list(s)
# print(d[1])
# print(d)
# print(len(d))

# if d[0] == 'a':
#  print('yes')

d = list(s)
for i in range(1, len(d), 2):
    if d[i] != 'a' and d[i] != 'b':
        d.pop(i)
        d.insert(i, 'a')
        # print(d)
    elif d[i] is 'a' or d[i] is 'b':
        d.pop(i)
        d.insert(i, 'c')
        # print(d)

print(d)
j = ''.join(d)
print(j)

# 8
# Дана строка. Если она начинается на 'abc', то заменить их на 'www',
# иначе добавить в конец строки 'zzz'.
print('====== 8 task =======')

# s = 'abcdefghijklmnopqrstuvwxyz'
s = 'in mask we trust'

# print(s[:3] == 'abc')
# print(s)

if s[:3] == 'abc':              # можна використати str.endswith(suffix[, start[, end]])
    res = s.replace('abc', 'www', 1)   # не вийшло, поки не присвоїла йншій змінній, Антон підказав
else:
    res = s + 'zzz'

# коли метод повертає копію рядка (списку, словаря), то цій копії треба присвоїти нову змінну

print(res)
# e = type(s[:3])
# print(e, s)
# s.replace('abc', 'www', 1)
# print(s)
# s = s + 'zzz'

# 9
# Дано две строки. Сравнить совпадают ли в них первые и последние 4 символа.
print('====== 9 task =======')
s1 = 'qui la voce sua soave'
# s2 = 'qui la voce sua soave'
s2 = 'la voce sua soave qui'

print(s1[:4])
print(s1[-4:])

if s1[:4] == s2[:4] \
        and s1[-4:] == s2[-4:]:
    print('they are identical')
else:
    print('no, no, no')

# 10
# Дана строка. Вывести средний символ в нижнем регистре.
print('====== 10 task =======')
s = 'PACE, PACEO MIO DIO!'
# difine if there is even or odd number of letters in the string
print(len(s))
# print(len(s)//2)
# print(s[-len(s)//2:])

ls = len(s)//2
if len(s)%2 == 0:
    s1 = s[ls - 1:]
    s2 = s1[:-ls + 1]
    print(s2)
    lo = s2.lower()
    print(lo)
    new_s = s[:ls - 1] + lo + s[-ls + 1:]
else:
    s1 = s[ls:]
    s2 = s1[:-ls]
    print(s2)
    lo = s2.lower()
    print(lo)
    new_s = s[:ls] + lo + s[-ls:]
print(new_s)

# or make this task using list?

# or with replace?