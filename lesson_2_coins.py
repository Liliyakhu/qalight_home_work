f3 = 7
f5 = 15

def steps (x, y):
    for i in range (1, x + 1):
        naym_kratne =  y * i
        steps = i
        if naym_kratne % x == 0:
            return steps
        
def my_fn(s):
    d5, m5 = divmod(s, f5)
    if not m5:
        return (0, d5)
    else:
        for i in range (steps(f3, f5)):
            d5 = d5 - i
            d3, m3 = divmod(m5 + i*f5, f3)
            if not m3:
                return (d3, d5)
            if m3 and d5 == 0:
                return ('impossible')
            else:
                d5 = d5 + i # можна і замінити на 1, але тільки при циклі 0,1,2
    return "impossible!"

for d in range(1, 200):
    print (d, my_fn(d))
