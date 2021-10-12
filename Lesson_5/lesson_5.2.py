with open ('lesson5_1.txt') as file:
    file_lines = file.readlines()
    str_count = 0
    for num, line in enumerate(file_lines):
        str_count += 1
        words = len(line.split())
        print(f'#{num +1} - {words}слов')
    print(f'{str_count} строк')
