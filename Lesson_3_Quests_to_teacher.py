print('-----Question 1-----')
print()

b = []

for i in [(1, 23, 4), 12, 'a']:
    if hasattr(i, '__len__'):
        for a in i:
            b.append(a)
    else:
        b.append(i)

print(b)

# the next DOESN'T WORK!
# b = [a if hasattr(i, '__len__') else i for i in [(1, 23, 4), 12, 'a'] for a in i]
# print(b)


b = [i for i in [(1, 23, 4), 12, 'a'] if hasattr(i, '__len__') and not isinstance(i, str)] # else a for a in i]
print(b)

print()
print('-----Question 2-----')
print()

o1 = map(lambda x: x * 2, range(10))  # the same as
o2 = (i * 2 for i in range(10))
print(o1)
print(o2)
print(list(o1)[2])
print(list(o2))
p = tuple(list(o2)) # this one doesn't work in RUN but works in console, why?
print(p)