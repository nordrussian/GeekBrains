with open ('lesson5_1.txt', 'w') as file:
    y = input('Введите строку: \n')
    while y:
        file.write(f'{y}\n')
        y = input('Введите строку: \n')

