a = int(input('Please, enter first number:'))
b = int(input('Please, enter second number:'))
c = int(input('Please, enter third number:'))

# 1 действие
if a and b and c:
    print("Нет нулевых значений!!!")
else:
    print('Есть хоть один ноль!!!')

# 2 действие 
first_not_null = a or b or c or 'Все нули!!!'
print('Первое ненулевое значение - ' + str(first_not_null))

# 3 и 4 действия
print('3 - ' + str(a - b - c) if a >= b + c else '4 - ' + str(b + c - a))

# 5 действие
if a > 50 and (b > a or c > a):
    print('Вася')

# 6 действие
if a>  5 or (b == 7 and c == 7):
    print('Петя')
