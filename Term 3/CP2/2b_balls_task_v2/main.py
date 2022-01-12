# 2 вариант. Номер 2 Б 

# А) Необходимо использовать список.
# В него удобно добавлять и удалять элементы.
# Нужно создать счётчик для элементов одного цвета.
# Когда он достигает 3х мы будем удалять 3 элемента.
# При добавлении каждого элемента нового цвета нужно проверить являются ли 2 предыдущие того же цвета.

# Вычислительная мощность - O(n) - линейное время

import os

os.system("cls")

def get_destroyed_balls(balls): 
    balls = balls.split() # Cформируем список

    balls_ammount = len(balls) # Получим кол. слов в списке (шариков)

    if balls_ammount == 0:
        return 0 # Нет шаров для уничтожения

    balls_duplicate = [] # Дубликат списка шариков.
    previous_ball = balls[0]
    same_balls_count = 1

    for current_ball in balls[1:]: # От эл. с индексом 1 до конца
        if current_ball == previous_ball:
            same_balls_count += 1

        elif same_balls_count < 3: # Не собрали 3 одинаковых. Попался новый цвет
            # Сохраним старые шары в отдельный список шаров
            balls_duplicate = balls_duplicate + [previous_ball] * same_balls_count 
            same_balls_count = 1

        else:
            same_balls_count = 1

        previous_ball = current_ball

    if same_balls_count < 3:
        balls_duplicate = balls_duplicate + [previous_ball] * same_balls_count
    
    # Уничтоженные шары = все шары - оставшиеся
    destroyed_balls = balls_ammount - len(balls_duplicate)

    if destroyed_balls == 0:
        return 0
    else:
        # Рекурсия
        # Она необходима для проверки списка на наличие шариков для уничтожения,
        # после уничтожения найденных шариков.
        return destroyed_balls + get_destroyed_balls(' '.join(balls_duplicate)) # Подавать как строку без [] и ,


# "кр кр син зел жел жел жел зел черн" - пример для ввода. 9 шаров
balls = input("Введите не более 10 элементов разных цветов: \n")

print("Было уничтожено шаров = " + str(get_destroyed_balls(str(balls))))

