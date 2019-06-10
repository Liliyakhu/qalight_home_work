# Скачиваем файл test_data.txt. Сохраняем файл в той же папке что и скрипт.
# 3. Найти производителя с наибольшим количеством товаров.


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
        result.add((s[0], s[1], s[2], float(s[3]), s[4]))
    else:
        # print(s)
        if s[3] == '':
            s.remove('')
            s[3] = s[3].replace(',', '.')
            s[3] = s[3].replace(' ', '')
            # print(s)
            result.add((s[0], s[1], s[2], float(s[3]), s[4]))
        else:
            s[2] = s[2] + s[3]
            s.remove(s[3])
            s[3] = s[3].replace(',', '.')
            s[3] = s[3].replace(' ', '')
            # print(s)
            result.add((s[0], s[1], s[2], float(s[3]), s[4]))

print('result', result)

li = list(result)
print('list', li)


def take_fourth(elem):
    return elem[3]

s = sorted(li, key=take_fourth)
# print(s)
for i in s:
    print(i)