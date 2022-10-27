'''
Задача на динамическое программирование!

План решения:
1. Посмотреть моё решение задачи с кузнечиком и марио.
2. Придумать алгоритм решения этой задачи на бумаге
'''

'''
if s < n.top() and s < m.top() - give answer
Резюме, которые забираю можно удалять из списков ??
Чтобы определить, какие резюме брать, нужно определить стоимость добраться до каждой.
Потом пойти от обратного?

Можно ли абстрагироваться от кол. стопок резюме, ведь их может быть и больше?
'''


import math

# s - бюджет
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

if smaller == 0: # Замены '-' производить не нужно
    lst_n = list(map(int, lst_n))
    lst_m = list(map(int, lst_m))
elif smaller > 0:
    lst_m = list(map(int, lst_m[:-smaller]))
    lst_m.extend([math.inf] * smaller)
    lst_n = list(map(int, lst_n))
elif smaller < 0:
    lst_n = list(map(int, lst_m[:smaller]))
    lst_n.extend([math.inf] * (m - n))
    lst_m = list(map(int, lst_m))

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

# Матрица возможных исходов
matrix = []

