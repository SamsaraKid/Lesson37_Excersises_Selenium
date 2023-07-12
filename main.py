# задача 1. процент в банке
def bank(a, percent, years):
    for y in range(years):
        a += a * percent / 100
    return int(a)


print(bank(500, 10, 10))


# задача 2. проверка даты
def date(day, mon, year):
    monthes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isinstance(year, int) and isinstance(mon, int) and isinstance(day, int):
        if 1 <= mon <= 12:
            if 1 <= day <= monthes[mon - 1]:
                return True
    return False


print('12, 10, 2000:', date(12, 10, 2000))
print('12, 13, 2000:', date(12, 13, 2000))
print('100, 1, 2000:', date(12, 13, 2000))
print('1, 1, qwer:', date(12, 13, 'qwer'))


# задача 3. убрать все заглавные

let = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
print('ЫгВЫоЯСремДШНККАыкЩЙФа', ''.join(list(filter(lambda x: x.islower(), let))))


# посчитать самую длину последовательность 1-ц
mas = '000000111111111111110000000000001011111110100111111111011111111110111111111110100000000000111111111000000101' \
      '00100111111110000000000000011111111111111111101111111111010111111111111110000000000000000000111101010011'

count = 0
res = 0
for m in mas:
    if m == '1':
        count += 1
    else:
        if count >= res:
            res = count
        count = 0

print(res)


