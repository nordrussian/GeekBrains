# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(a, b):
    if b == 0:
        print('На ноль делить нельзя')
    else:
        return a / b


a = int(input('Введите число a:'))
b = int(input('Введите число b:'))
print(my_func(a, b))