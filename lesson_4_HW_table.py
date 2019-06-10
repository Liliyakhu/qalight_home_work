# Есть строка.
# Необходимо написать две функции.
#
#	f1 - должна возвращять структуру следующего вида:
#	{
#	  (('group', 1), ('symbol', 001), ('kekd', '22012600'), ...)
#	}
#	Возвращать необходимо только те записи у которых сумма больше 0

#	f2 - должна возвращять структуру следующего вида:
#	[
#	  (('group', 1), ('symbol', 001), ('kekd', '2201'), ...)
#	]
#	Записи у которых совпадают первые 4 символа kekd должны быть сгруппированы.


f = open('/home/korvin/Картинки/Qalight/Lesson_4/Lesson_4_HW_text.txt', 'r', encoding = 'utf-8')
text = f.readlines()
f.close()
# print(text)
len_of_text = len(text)
# print(len_of_text)
needed_text = text[5:len_of_text-3]
# print(len(needed_text))
print(needed_text)

# візьму один елемент списка
# 10 пробілів до групи, 6 пробілів до символа, 3 пробіла до КЕКД,
# мін 15, макс. 19 (там де 0,00) пробілів до суми,
# мін 4, макс. 15 пробілів до нарост. підс.


def f1(text_list):
    result = set()
    not_result = set()
    for i in text_list:
        new = i.strip()
        group = new[0]
        symbol = new[7:10]
        kekd = new[13:21]
        s = new[36:48]
        summa = s.replace(' ', '')
        n = new[52:68]
        narost = n.replace(' ', '')
        if summa != '0,00':
            result.add((('group', group), ('symbol', symbol),
            ('kekd', kekd), ('summa', summa), ('narost', narost)))
        elif summa == '0,00':
            not_result.add(symbol)
    #print(result)
    for i in result:
        print(i)
    # print(len(result))
    # print(len(not_result))


# f1(needed_text)

print('--------------------------------------')

def f2(text_list):
    result = set()
    for i in text_list:
        new = i.strip()
        group = new[0]
        symbol = new[7:10]
        kekd = new[13:17]
        s = new[36:48]
        summa = s.replace(' ', '')
        n = new[52:68]
        narost = n.replace(' ', '')
        result.add((('group', group), ('symbol', symbol),
        ('kekd', kekd), ('summa', summa), ('narost', narost)))
    print(result)
    set_in_list = list(result)
    # print(set_in_list)
    def take_second_of_third(elem):  # https://www.programiz.com/python-programming/methods/built-in/sorted
        # print(elem[2][1])
        return elem[2][1]
    sorted_list = sorted(set_in_list, key=take_second_of_third)
    print(sorted_list)
    for i in sorted_list:
        print(i)

f2(needed_text)