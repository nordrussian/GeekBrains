my_list = [7, 5, 3, 3, 2]

rating = int(input('Введите значение рейтинга: '))
inserted = False
for index, elem in enumerate(my_list):
    if rating > elem:
        my_list.insert(index, rating)
        inserted = True
        break

if not inserted:
    my_list.append(rating)

print(my_list)