# Скачиваем файл test_data.txt. Сохраняем файл в той же папке что и скрипт.
# 5. Написать функции которые будут отфильтровывать эту структуру по номеру модели,
# фразе у наименовании, цене, или количеству (не менее чем) и возвращать её же,
# но с отфильтроваными данными.

f = open('./text_data.txt')
text = f.readlines()
# s = ''.join(f.readlines())  # Наш файл записаный в строку. Эту переменную мы будем использовать дальше.

# print(text)
f.close()

result = set()

for i in text:
    s = i.replace('"', '')
    s = s.split(';')
    # print(len(s))
    # print(s)
    if len(s) == 6:
        s[3] = s[3].replace(',', '.')
        s[3] = s[3].replace(' ', '')
        result.add((s[0], s[1], s[2], float(s[3]), float(s[4])))
    else:
        # print(s)
        if s[3] == '':
            s.remove('')
            s[3] = s[3].replace(',', '.')
            s[3] = s[3].replace(' ', '')
            # print(s)
            result.add((s[0], s[1], s[2], float(s[3]), float(s[4])))
        else:
            s[2] = s[2] + s[3]
            s.remove(s[3])
            s[3] = s[3].replace(',', '.')
            s[3] = s[3].replace(' ', '')
            # print(s)
            result.add((s[0], s[1], s[2], float(s[3]), float(s[4])))

# print('result', result)

li = list(result)
print('list', li)


def take_elem(elem):
    return elem[1]

s = sorted(li, key=take_elem) # можна посортувати за різними елементами -
# - (фірма, модель, товар, ціна, кількість)

print(s)

# for i in s:
    # print(i)

# щоб вибрати певний діапазон кількості чи цін:
for i in s:
    if i[3] > 5 and i[3] < 100:
        print(i)





