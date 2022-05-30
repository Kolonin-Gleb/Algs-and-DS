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


# Лучшие способы добраться до каждого столбца от следующей точки до точки назначения 
def price_to_get(cur_position, target_position, k, prices):


    # размер списка = длине prices до target_position включительно.
    # Стоимость добраться в элементы, что находятся до тек. позиции включительно = -math.inf
    # т.к. в них нельзя добраться (назад идти нельзя)
    price_to_come = [-math.inf] * (target_position + 1)
    # Это облегчит работу с индексами при дальнейших расчётах

    next_position = cur_position + 1


    # Определение Лучших способов добраться в те позиции, до которых можно сразу допрыгнуть
    for i in range(next_position, cur_position + k + 1):
        # Прямой способ добраться до позиции всегда самый выгодный, т.к. все предыдущие элементы < 0
        price_to_come[i] = prices[i]

    # Определение лучших способов добраться в удаленные позиции. y - индекс удалённой позиции
    for y in range(cur_position + k + 1, target_position + 1):
        # Сохраняю все стоимости добаться до позиции
        possible_prices = []
        for j in range(y-k, y): # Рассматриваю стоимость добраться из k предыдущих
            possible_prices.append(price_to_come[j] + prices[y])
        price_to_come[y] = max(possible_prices)

    #print(price_to_come)
    return price_to_come

# Функция вычисления пути в target_position
# Будет возращать список to_be_visited отсортированный по возрастанию

# TODO: В этой функции можно обойтись без target_position используя len(price_to_come)
def path_to_target(cur_position, prices, price_to_come):
    to_be_visited = [len(price_to_come) - 1] # Индексы элементов, соответствующие индексам в prices, которые нужно посетить
    cur_target = to_be_visited[-1]

    # j - индекс, на который производится попытка прыгнуть

    while cur_position < cur_target - k: # Пока до тек. положения нельзя допрыгнуть
        for j in range(cur_target-k, cur_target): # Рассматриваю стоимость добраться из k предыдущих
            if price_to_come[j] + prices[cur_target] == price_to_come[cur_target]:
                to_be_visited.append(j)
                cur_target = to_be_visited[-1]
                break
            #else: # Рассмотрим более близкие элементы
            #    break # Не continue, т.к. нужно заново инициализировать переменную цикла, т.е. заново запустить цикл

    to_be_visited.sort() # Чтобы идти из начала в конец
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
        continue # Снова рассматриваю все возможные способы перемещения

    # Получаю лучшие способы добраться до каждого столбца от следующей точки до точки назначения 
    price_to_come = price_to_get(cur_position, target_position, k, prices)
    # Сохранив их в price_to_come я буду выбирать максимальное для посещения идя с конца

    to_be_visited = path_to_target(cur_position, prices, price_to_come)

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

