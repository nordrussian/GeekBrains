nums = {
    'One' : 'Один',
    'Two' : 'Два',
    'Three' : 'Три',
    'Four' : 'Четыре',
    }

with open('lesson5.4.txt') as file, open ('new_lesson5.4.txt', 'w') as new_file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        rus_num = nums.get(data[0])
        new_file.write(f'{line.replace(data[0], rus_num)}') 