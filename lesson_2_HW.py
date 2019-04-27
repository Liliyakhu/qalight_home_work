
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

l = []
while 'i' in s:
    h = s.rfind('i')
    # print(h + 1)
    l.append(str(h + 1))
    s = s[:h]
    # print(s)

# print(l)
v = ', '.join(reversed(l))
print(v)

# 4
# Дана строка. Определите, какой символ в ней встречается
# раньше: 'x' или 'w'. Если какого-то из символов нет,
# вывести сообщение об этом.
# нужно использовать конструкцию ветвления if-elif-else
print('====== 4 task =======')
s = 'jhkjkoiwejkh kjahlskdjfh  qwkjhlk zkjh kjhaswdefxkjh jkjhkjh'

k = s.find('x')
l = s.find('w')
#print('In \'',s,'\'')
print('In \'%s\'' % s)

if k > l:
    print('\'w\' is the first, not \'x\'')
elif k < l:
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
s = 'abra cadabra' #Nisl scelerisque justo per hac ras purus lectus maecenas litora facilisi potenti'

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
        print(d)
    elif d[i] is 'a' or d[i] is 'b':
        d.pop(i)
        d.insert(i, 'c')
        print(d)

print(d)
