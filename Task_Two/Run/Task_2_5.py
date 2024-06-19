print('Деление -', 24 / 2)
print('Целочисленное деление // -', 25 // 2)
print('Остаток от деления % -', 25 % 2)
print('Возведение в степень ** -', 2 ** 3)

print(23 // 7)
print(20 // 5)
print(2 // 5)
print(123 // 10)
print(-123 // 10)

print(23 % 7)
print(20 % 5)
print(2 % 5)
print(123 % 10)

a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)

a = 82 // 3 ** 2 % 7
print(a)

# Task 1
b = int(input())
q = int(input())
n = int(input())
print(b * q ** (n - 1))

# Task 2
cm = int(input())
m = cm // 100
print(m)

# Task 3
people = int(input())
orange = int(input())
print(orange // people)
print(orange-(people*(orange // people)))

# Task 4
n = int(input())
print((n // 2) + (n % 2))

# Task 5
time_minute = int(input())
print(time_minute, 'мин - это', time_minute // 60, 'час', time_minute % 60, 'минут.')

# Task 6
num = int(input())
print(int(-(-(num / 4) // 1)))

# Task 7
num = int(input())
a = num // 100
b = (num // 10) % 10
c = num % 10
summ = a + b + c
multi = a * b * c
print('Сумма цифр =', summ)
print('Произведение цифр =', multi)

# Task 8
num = int(input())
a = num // 100
b = (num // 10) % 10
c = num % 10
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')

# Task 8
num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num % 100) // 10
d = num % 10
print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)

# Task 9
num = int(input())
a = num // 10000
b = (num // 1000) % 10
c = (num // 100) % 10
d = (num % 100) // 10
e = num % 10
print(a, b, c, d, e)

print('*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', sep='')
print('*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', sep='')
print('*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', sep='')
print('*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', sep='')

a = int(input())
b = int(input())
print('Квадрат суммы', a, 'и', b, 'равен', (a + b) * (a + b))
print('Сумма квадратов', a, 'и', b, 'равна', a * a + b * b)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a ** b + c ** d)

n = int(input())
print(n + n * 11 + n * 111)
