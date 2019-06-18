# Распаковать архив и прочитать в конце архива ссылку
# на видеосравнение java и python. Файл можно получить в чате группы

import zipfile

source = '/home/korvin/Завантаження/2_51950754678072944775604766623483440850.zip'
res = 'No data found'

with zipfile.ZipFile(source, 'r') as z:
    z.printdir()
    s = z.namelist()
    file = z.open(s[0], 'r')

    file.seek(-2048, 2)
    res = file.read(2048)
    file.close()

    # search URL like string
    pos = res.find('http://'.encode())
    if (pos == -1):
        pos = res.find('https://'.encode())
    else:
        pos = res.find('ftp://'.encode())
    out = res[pos:].decode()
print(out)