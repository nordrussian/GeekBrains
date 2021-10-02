# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = input("Введите данные для формирования списка: ")

input_my_list = my_list.split()

len_list = len(input_my_list)
el = 0
if len_list > 1:
    while el < len_list - 1:
        input_my_list[el], input_my_list[el+1] = input_my_list[el+1], input_my_list[el]
        el += 2



print(input_my_list)
 