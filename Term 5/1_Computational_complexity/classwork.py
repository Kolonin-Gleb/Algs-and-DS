# Идеи по реализации
'''
Наивный подход - просто идти по списку и менять всех на Правую или Левую ногу

Идея с оптимизацией, но не лучашя:
Посчитать размер групп.
Желтые и Розовые.
Кричать для тех, каких групп меньше.

Лучшее решение:
# Количество 2ых групп либо равно либо на 1 меньше, чем первых!
# Натыкаясь на 2ую группу необходимо кричать первой менять ногу!
'''

#       0    1    2    3    4    5    6    7    8    9
inp = ['R', 'R', 'L', 'L', 'L', 'R', 'L', 'L', 'L', 'R'] # 
# Должен быть выход:
# С 2 по 4
# С 6 по 8

cur_group = inp[0]

indexes_for_command = []

for el_ind in range(len(inp)): # Иду по индексам, т.к. по ним предстоит давать команды
    if cur_group != inp[el_ind]: # Наткнулся на новую группу
        cur_group = inp[el_ind]
        indexes_for_command.append(el_ind)

        if len(indexes_for_command) == 2:
            print(f"С {indexes_for_command[0]} по {indexes_for_command[1]-1} меняй ногу!")
            indexes_for_command.clear()

# TODO: Без повторения куска кода!

if indexes_for_command: # Если не пустой - 
    indexes_for_command.append(len(inp))
    print(f"С {indexes_for_command[0]} по {indexes_for_command[1]-1} меняй ногу!")

