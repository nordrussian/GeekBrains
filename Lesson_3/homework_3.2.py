# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, year, city, mail, tel):
    print(f'{name} {surname} {year} {city} {mail} {tel}')
    

name = input('Введите Ваше имя:')
surname = input('Введите Вашу фамилию:')
year = input('Введите Ваш год рождения:')
city = input('Введите Ваш город:')
mail = input('Введите Вашу почту:')
tel = input('Введите Ваш телефон:')
print(my_func(name = name, surname = surname, year = year, city = city, mail = mail, tel = tel))