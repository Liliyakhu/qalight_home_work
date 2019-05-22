# 1
# Дан упорядоченный список книг.
# Добавить новую книгу, сохранив упорядоченность списка.
print('====== 1 task =======')

s = 'abcdefghijklnopqrstuvwxyz'

li = list(s)
# print(li)

li.append('m')
# print(li)

li.sort()
print(li)

# 2
# Дан список состоящий чисел.
# Выяснить сколько раз входит ли некоторое число в список.
print('====== 2 task =======')

a = [3, 7, 35, 45, 67, 68, 45, 73, 345]
b = a.count(45)
print(b)

# 3
# Найдите сумму четных чисел списка которые являются числом.
print('====== 3 task =======')

a = [3, 'd', [35, 46], 67, 'the weather is good', 68, 45, 74, 345.5]
# print(a[2])
# print(len(a))

# if str(a[5]).isdigit():
    # print('yes')

# if a[4] % 2 == 0:
    # print('yes')

sum = 0
for i in range(0, len(a)):
    if str(a[i]).isdigit() and a[i]% 2 == 0:
        sum += a[i]
        # print(sum)

print(sum)

# 4
# Дан пустой список. Заполнить список путем ввода данных с клавиатуры.
# Найти наибольший элемент списка.
print('====== 4 task =======')

a = []
# a.append(2)
# print(a)

for i in range(0, 10):
    c = input('print something\n')
    # if c.isalpha():
    a.append(c)
    # elif c.isdigit():
        # a.append(int(c))

print(a)
a.sort()
print(a)

# 5
# Создайте объект, который мог бы описать журнал посещаимости.
# Измените информацию о посещаимости второму студенту в списке.
# Отформатиройте вывод журнала.
print('====== 5 task =======')

journal = [
    ['Name1', [['21-02', True], ['25-02', False]]],
    ['Name2', [['21-02', False], ['25-02', True]]],
    ['Name3', [['21-02', True], ['25-02', True]]],
    ['Name4', [['21-02', True], ['25-02', False]]]
]

# print(journal[1])
second = journal[1]
# print(second[1])
sec_in_sec = second[1]
# print(sec_in_sec[1])
s_in_s_in_s = sec_in_sec[1]
# print(s_in_s_in_s[1])
s_in_s_in_s[1] = False
# print(journal)

# or

journal[1][1][1][1] = True
print(journal)

# d = dict(journal)
# print(d)

# print(len(journal))

def vyvod(list):
    for i in range(len(list)):
        print(list[i][0] + ':')
        if True in list[i][1][0]:
            print('  ', list[i][1][0][0], '+')
        else:
            print('  ', list[i][1][0][0], '-')
        if True in list[i][1][1]:
            print('  ', list[i][1][1][0], '+')
        else:
            print('  ', list[i][1][1][0], '-')

vyvod(journal)