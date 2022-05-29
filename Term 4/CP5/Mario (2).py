import math


# (На вход подаются числа N и K и количество получаемых монет для каждого столбика (положительное или отрицательное), 

# выход – наибольшее количество монет, которое может собрать Марио,
# номера всех столбиков, которые посетил Марио.
# число прыжков Марио (= кол. посещённых столбиков)

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

target_position = n - 1 # Индекс столбца, куда нужно добраться. По умолчанию = последнему столбцу
cur_position = 0 # Текущее положение Марио
visited = [0] # Я буду сохранять индексы посещённых столбиков. Когда попросят вывести номера я просто +1 ко всем


# Лучший способ добраться до каждого столбца от следующей точки до точки назначения 
def price_to_get(cur_position, target_position, k, prices):

    price_to_come = [-math.inf] * (target_position - cur_position)

    next_position = cur_position + 1

    # Определение Лучших способов добраться в те позиции, до которых можно сразу допрыгнуть
    for i in range(next_position, cur_position + k + 1): #TODO: Как быть, если k = 1?
        # Прямой способ добраться до позиции всегда самый выгодный, т.к. все предыдущие элементы < 0
        price_to_come[i - 1] = prices[i]

    # Определение лучших способов добраться в удаленные позиции
    for y in range(cur_position + k + 1, target_position + 1):
        # Сохраняю все стоимости добаться до позиции
        possible_prices = []
        for j in range(y-k-1, y - 1): # Рассматриваю k предыдущих цен
            possible_prices.append(price_to_come[j] + prices[y]) # TODO: Проблема с индексами prices
        price_to_come[y - 1] = max(possible_prices)

    #print(price_to_come)
    return price_to_come

# Функция перемещения вычисления пути в target
# Будет возращать список to_be_visited отсортированный по возрастанию
def path_to_target(cur_position, target_position, price_to_come):
    to_be_visited = [target_position]

    while cur_position != target_position:
        for j in range(k, 0, 1): # От самых дальних к ближним. 
            if to_be_visited[-1] - j >= 0: # Если настолько удалённый элемент существует
                if price_to_come[to_be_visited[-1] - j] + prices[target_position] == price_to_come[target_position]:
                    to_be_visited.append(target_position - j)
                    target_position = target_position - j
                    break
            else: # Рассмотрим более близкие элементы
                continue

    return to_be_visited
    


while cur_position != (n - 1): # Пока не на последнем столбике
    
    # Поиск ближайшего + элемента от следующей позиции до последнего столбца
    # Если индекс не будет найден, значит Задача - попасть в посл. эл.
    for column in range(cur_position + 1, n):
        if prices[column] >= 0:
            target_position = column
            break

    #print(target_position)


    if target_position <= (cur_position + k): # Если есть 0+ элемент, до которого можно добраться, то сразу делаю это 
        cur_position = target_position
        visited.append(cur_position)
        wallet += prices[cur_position]
        # Снова рассматриваю все возможные способы перемещения

    # Получаю лучшие способы добраться до каждого столбца от следующей точки до точки назначения 
    price_to_come = price_to_get(cur_position, target_position, k, prices)
    # Сохранив их в price_to_come я буду выбирать максимальное для посещения идя с конца

    price_to_come.append(0, 0) # Добавление в начало списка 0. Т.к. оставаться в тек. позиции ничего не стоит.
    # Это упростит работу с индексами при дальнейших расчётах.

    print(price_to_come)

    to_be_visited = path_to_target(cur_position, target_position, price_to_come)

    print(to_be_visited)

    # Перемещение в target_position
    for position in to_be_visited:
        cur_position = position
        visited.append(cur_position)
        wallet += prices[cur_position]

    

print("Наибольший капитал Марио = " + str(wallet))
print("Посещённые столбики: ")
for i in range(len(visited)):
    visited[i] = visited[i] + 1
print(visited)
print("Число посещённых столбиков = " + str(len(visited)))

