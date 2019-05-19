import decimal

# 1
# Пользователь вводит два числа.
# найдите сумму и произведение данных чисел.
print('====== 1 task =======')

# https://stackoverflow.com/questions/46647744/checking-to-see-if-a-string-is-an-integer-or-float

x = input('Enter a number:\n')
if x.isdigit():
    x = int(x)
elif x.replace('.', '', 1).isdigit() and x.count('.') < 2:
    x = float(x)
else:
    print('It is Neither Integer Nor Float! Something else')

y = input('Enter another number:\n')
if y.isdigit():
    y = int(y)
elif y.replace('.', '', 1).isdigit() and y.count('.') < 2:
    y = float(y)
else:
    print('It is Neither Integer Nor Float! Something else')

suma = x + y
print(suma)
prod = x * y
print(prod)

# or
# у цьому варіанті, якщо вводять щось не те, то відразу друкується відповідь і дії не продовжуються


x = input('Enter a number:\n')
if x.isdigit():
    y = input('Enter another number:\n')
    if y.isdigit():
        suma = int(x) + int(y)
        prod = int(x) * int(y)
        print('Sum is:', suma)
        print('Product is:', prod)
    elif y.replace('.', '', 1).isdigit() and y.count('.') < 2:
        suma = int(x) + float(y)
        prod = int(x) * float(y)
        print('Sum is:', suma)
        print('Product is:', prod)
    else:
        print('It is Neither Integer Nor Float! Something else')
elif x.replace('.', '', 1).isdigit() and x.count('.') < 2:
    y = input('Enter another number:\n')
    if y.isdigit():
        suma = float(x) + int(y)
        prod = float(x) * int(y)
        print('Sum is:', suma)
        print('Product is:', prod)
    elif y.replace('.', '', 1).isdigit() and y.count('.') < 2:
        suma = float(x) + float(y)
        prod = float(x) * float(y)
        print('Sum is:', suma)
        print('Product is:', prod)
    else:
        print('It is Neither Integer Nor Float! Something else')
else:
    print('It is Neither Integer Nor Float! Something else')


# print('Sum is:', suma)
# print('Product is:', prod)

# 2
# Пользователь вводит число.
# Выведите на экран квадрат этого числа, куб этого числа.
print('====== 2 task =======')

x = input('Enter a number:\n')

if x.isdigit():
    print(int(x)**2)
    print(int(x)**3)
else:
    print(float(x) ** 2)
    print(float(x) ** 3)    # чому, коли ввести 1.2, то куб виходить 1.7279999999999998, як цього уникнути?

# 3
# Пользователь вводит три числа.
# Увеличьте первое число в два раза, второе числа уменьшите на 3,
# третье число возведите в квадрат и затем найдите сумму новых трех чисел.
print('====== 3 task =======')

x = input('Enter a number:\n')
if x.isdigit():
    x = int(x) * 2
else:
    x = float(x) * 2
print('x =', x)

y = input('Enter a number:\n')
if y.isdigit():
    y = int(y) - 3
else:
    y = float(y) - 3
print('y =', y)

z = input('Enter a number:\n')
if z.isdigit():
    z = int(z) ** 2
else:
    z = float(z) ** 2
print('z =', z)

print('sum is', x+y+z)

# if x.isdigit():
#    x = int(x) * 2
#    if y.isdigit():
#        y = int(y) - 3
#        if z.isdigit():
#            z = int(z) ** 2
#            s = x + y + z
#            print(x, y, z, s)
#        else:
#
#    else:
#        y = float(y) - 3
# else:
#    x = float(x) * 2

# 4
# Пользователь вводит три числа. Найдите среднее арифметическое этих чисел,
# а также разность удвоенной суммы первого и третьего чисел
# и утроенного второго числа.
print('====== 4 task =======')

x = input('Enter a number:\n')
if x.isdigit():
    x = int(x)
else:
    x = float(x)
print('x =', x)

y = input('Enter a number:\n')
if y.isdigit():
    y = int(y)
else:
    y = float(y)
print('y =', y)

z = input('Enter a number:\n')
if z.isdigit():
    z = int(z)
else:
    z = float(z)
print('z =', z)

a = (x+y+x)/3
print(a)

b = (2 * (x + z)) - 3 * y
print(b)

# Enter a number:
# 1.2
# x = 1.2
# Enter a number:
# 1.3
# y = 1.3
# Enter a number:
# 1.4
# z = 1.4
# 1.2333333333333334 ??????????
# 1.299999999999999  ??????????????

# seen 1 week after, should use decimal.Decimal

# 5
# Пользователь вводит сторону квадрата. Найдите периметр и площадь квадрата.
print('====== 5 task =======')

x = input('Enter side of a square:\n')
x = x.replace(',', '.', 1)
x = decimal.Decimal(x)

p = 4 * x
s = x ** 2
print('Perimetr is', p)
print('Area is', s)

# 6
# Пользователь вводит цены 1 кг конфет и 1 кг печенья.
# Найдите стоимость:
# а) одной покупки из 300 г конфет и 400 г печенья;
# б) трех покупок, каждая из 2 кг печенья и 1 кг 800 г конфет.
print('====== 6 task =======')

dec = decimal.Decimal

candy_price = input('Enter price of candies, UAH per kilo:\n')
candy_price = candy_price.replace(',', '.', 1)
candy_price = dec(candy_price)

cookies_price = input('Enter price of cookies, UAH per kilo:\n')
cookies_price = cookies_price.replace(',', '.', 1)
cookies_price = dec(cookies_price)

a = candy_price * dec('0.3')\
    * cookies_price * dec('0.4')

# https://stackoverflow.com/questions/7560455/decimals-to-2-places-for-money-in-python-3

cents = dec('.01')
money_1 = a.quantize(cents, decimal.ROUND_HALF_UP)
print('One purchase - 300 gram of candies and 400 gram of cookies costs:\n',money_1)
# як позбутися відступа при виводі money_1 ?
b = dec('3') * (candy_price * dec('2') * cookies_price * dec('1.8'))
money_2 = b.quantize(cents, decimal.ROUND_HALF_UP)
print('Three purchases - 2 kilos of candies and 1.8 kilos of cookies cost:\n',money_2)

# 7
# Пользователь вводит время в минутах и расстояние в километрах.
# Найдите скорость в м/c.
print('====== 7 task =======')

dec = decimal.Decimal

time = input('Enter time, minutes:\n')
time = time.replace(',', '.', 1)
time = dec(time)

dist = input('Enter distance, kilometers:\n')
dist = dist.replace(',', '.', 1)
dist = dec(dist)
dist_met = dist * dec('1000')

speed = dist_met / time
speed = speed.quantize(dec('0.01'), decimal.ROUND_HALF_UP)
print('Speed is', speed, 'meters per minute.')

# 8
# Даны катеты прямоугольного треугольника.
# Найдите площадь, периметр и гипотенузу треугольника.
print('====== 8 task =======')

dec = decimal.Decimal

a = dec('10')
b = dec('12')

# c = √a**2+b**2
c = (a ** dec('2') + b ** dec('2')) ** dec('0.5')
c = c.quantize(dec('0.01'), decimal.ROUND_HALF_UP)
print(c)

p = dec(a) + dec(b) + dec(c)
p = p.quantize(dec('0.01'), decimal.ROUND_HALF_UP)
print(p)

# S = 1/2*a*b
s = dec('0.5') * a * b
s = s.quantize(dec('0.01'), decimal.ROUND_HALF_UP)
print(s)

p = dec(a) + dec(b) + dec(c)
p = p.quantize(dec('0.01'), decimal.ROUND_HALF_UP)
print(p)

# 9
# Дано значение температуры в градусах Цельсия.
# Вывести температуру в градусах Фаренгейта.
print('====== 9 task =======')

# Цельсий х 1,8 + 32 = Фаренгейт

dec = decimal.Decimal
c = dec('15')
f = c * dec('1.8') + dec('32')
print(f)
f = f.quantize(dec('0.01'), decimal.ROUND_HALF_UP)
print(f)