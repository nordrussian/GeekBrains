# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict.

season_dict = {1 : "winter", 2 : "spring", 3 : "summer", 4 : "winter"}
season_list = ["winter", "spring", "summer", "winter"]
month = int(input('Введите номер месяца: '))
if month == 1 or month == 2 or month == 12:
    print(season_dict.get(1))
    print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_dict.get(2))
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get(2))
    print(season_list[2])
elif month == 9 or month == 10 or month == 11:
    print(season_dict.get(2))
    print(season_list[3])
else:
    print ("Такого месяца нету!!!")