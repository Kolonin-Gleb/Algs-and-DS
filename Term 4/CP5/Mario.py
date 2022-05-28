import math


# (На вход подаются числа N и K и количество получаемых монет для каждого столбика (положительное или отрицательное), 
# выход – наибольшее количество монет, которое может собрать Марио,
# число прыжков Марио 
# номера всех столбиков, которые посетил Марио.


print("Введите кол. столбиков") # от 1 до ...
n = int(input())


prices = []
for i in range(n):
    print("Сколько монет (+ / -) на столбике " + str(i + 1) + " ?")
    prices.append(int(input()))
# print(prices)

print("Введитие максимальный прыжок") # от 1 до ...
k = int(input())

# Максимальное число монет, что соберёт Марио
wallet = prices[0] # Изначально его бюджет = сумме на 1 столбике

position = 0 # Текущее положение Марио
target_position = n - 1 # Индекс столбца, куда нужно добраться. По умолчанию = последнему столбцу


# Данная функция определяет стоимость добраться до всех элементов price_to_come
def price_to_get(price_to_come, k):
    # Вычислю число способов попасть в каждую позицию
    # Это что-то вроде БАЗЫ
    ways_to_come = [1] * len(price_to_come) # Есть как минимум 1 способ добраться в каждую позицию

    # Число способов добраться до позиции = сумме способов добраться до позиций из которых можно попасть в эту
    for i in range(len(price_to_come)):
        # Если позади элементов меньше, чем возможность прыжка
        # То суммируем значения тех эл., что имеются и +1, т.к. можно допрыгнуть из тек. положения
        if i < k:
            ways_to_come[i] = 



        # Иначе
        # Суммируем значения предыдущих k элементов

        # Попытка посчитать сумму способов добраться до предыдущих позиций
        try:
            sum_of_ways = 0
            for j in range(k):
                sum_of_ways += ways_to_come[j]
        # Нет возможности посчитать сумму способов добраться до предыдущих позиций => эти позиции первые
        except:
            ways_to_come.append(i + 1)





while position != n: # Пока не на последнем столбике
    
    # Поиск ближайшего + элемента от следующей позиции до последнего столбца
    # Если индекс не будет найден, значит Задача - попасть в посл. эл.
    for column in range(position + 1, n):
        if prices[column] >= 0:
            target_position = column
            break

    #print(target_position)

    # Стоимость добраться до каждого столбца до точки назначения
    price_to_come = [-math.inf] * (target_position - position) 

    # Определяю стоимости добраться до каждого столбца
    price_to_get(price_to_come, k)

    break

    #for i in range(k): # Рассматриваю все возможные способы перемещения

    #    if prices[i] >= 0: # Если ближайшая ступенька не в убыток
    #        position += i
    #        wallet += prices[position]
    #        break # Снова рассматриваю все возможные способы перемещения
    #    else:
    #        # Сохранить, что это может быть выгодным
    #        pass
    
    
