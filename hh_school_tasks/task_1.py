import math

# n и m - кол. резюме в стопках
# s - бюджет
n, m, s = map(int, input().split()) 

# Списки с зарплатами резюме в каждой стопке
lst_n = []
lst_m = []

# input 1 - correct
'''
3 4 11
1 1
2 2
3 3
- 4
'''
# input 2 - correct
'''
5 5 10
5 1
1 3
1 3
1 3
1 3
'''
# input 3 - correct
'''
6 4 10
4 2
2 1
4 8
6 5
1 -
7 -
'''
# my input 1 - correct
'''
1 1 9
10 20
'''

# Ввод данных от пользователя.
cv_max_count = max(n, m)
for i in range(cv_max_count):
    inp = input().split()

    lst_n.append(inp[0])
    lst_m.append(inp[1])

# Убрать все '-' в меньшей стопке
# Привести тип данных стоимости резюме

smaller = n - m # 6 - 4
if smaller == 0: # Замены '-' производить не нужно
    lst_n = list(map(int, lst_n))
    lst_m = list(map(int, lst_m))
elif smaller > 0:
    lst_m = list(map(int, lst_m[:-smaller]))
    lst_n = list(map(int, lst_n))
elif smaller < 0:
    lst_n = list(map(int, lst_m[:smaller]))
    lst_m = list(map(int, lst_m))

print("lst_n", lst_n)
print("lst_m", lst_m)
print()


# Матрица возможных исходов
matrix = []

# Заготовка - матрица пустышка размером m+1 на n+1
for i in range(m+1):
    matrix.append([0] * (n+1))

# Установка исходных стоимостей добраться до каждого резюме из стопкок в матрицы
# при взятии резюме только из этой стопки

# Заполнение 1ой строки матрицы
for i in range(1, n+1):
    matrix[0][i] = sum(lst_n[:i])

# Заполнение 1ого столбца матрицы
for i in range(1, m+1):
    matrix[i][0] = sum(lst_m[:i])

# Иду по строкам матрицы возможных исходов, 
# чтобы определить макс. кол. резюме, что можно собрать
max_cv_collected = 0

# Для рассчёта стоимости взятия резюме, соответствующих индексам i j
# Использую непосредственные стоимости этих резюме.
# Добавляю 0, чтобы размерности совпали с представлением матрицы
lst_n.insert(0, 0) 
lst_m.insert(0, 0) 

# алгоритм рассчёта стоимости взятия резюме, соответствующих индексам i j
for i in range(0, m+1):
    for j in range(1, n+1):
        if s >= matrix[i][j-1] + lst_n[j]: # Если купить это резюме можно
            # Вычисляю стоимость взятия этого резюме
            matrix[i][j] = matrix[i][j-1] + lst_n[j] # Стоимость взятия предыдущих + нового
            if i + j > max_cv_collected:
                max_cv_collected = i + j
        else:
            break
            
print()
# output full matrix template
for row in matrix:
    print(row, sep='\n')

print("Можно взять ", max_cv_collected, " резюме")
