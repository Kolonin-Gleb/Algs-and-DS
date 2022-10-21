# Первая строка – целые числа n, m и s через пробел
'''
if s < n.top() and s < m.top() - give answer
Резюме, которые забираю можно удалять из списков ??
Чтобы определить, какие резюме брать, нужно определить стоимость добраться до каждой.
Потом пойти от обратного?

Можно ли абстрагироваться от кол. стопок резюме, ведь их может быть и больше?
'''


import math

n, m, s = map(int, input().split()) 

# Списки с зарплатами в стопках резюме
lst_n = []
lst_m = []


# Ввод данных от пользователя.
cv_max_count = max(n, m)
for i in range(cv_max_count):
    inp = input().split()

    lst_n.append(inp[0])
    lst_m.append(inp[1])

# Замена всех '-' в меньшей стопке на math.inf
smaller = n - m # 6 - 4

if smaller == 0:
    pass # Замены '-' производить не нужно
elif smaller > 0:
    lst_m = list(map(int, lst_m[:-smaller]))
    lst_m.extend([math.inf] * smaller)
elif smaller < 0:
    lst_n[smaller:] = [math.inf] * (m - n)

print(lst_m)
print()
print(lst_n)

# input 1
'''
3 4 11
1 1
2 2
3 3
- 4
'''
# input 3
'''
6 4 10
4 2
2 1
4 8
6 5
1 -
7 -
'''


"""
# Замену '-' можно оптимизировать потом
if inp[0] == '-':
    lst_n.append(math.inf)
else:
    lst_n.append(inp[0])
if inp[1] == '-':
    lst_m.append(math.inf)
else:
    lst_m.append(inp[1])

cv_taken = 0

# while s >= 

print(cv_taken)
"""


# На первом шаге всегда берем наименьший.
# Если одна из стопок полностью разобрана, а деньги остаются - берём из второй, пока есть возможность
# -- Это можно реализовать замени все '-' на math.inf


'''
Мне кажется, что эта задача на динамическое программирование!

План решения:
1. Посмотреть моё решение задачи с кузнечиком и марио.
2. Придумать алгоритм решения этой задачи на бумаге
'''
