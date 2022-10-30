# import math

# lst = [math.inf] * 5
# print(lst)


# test input

lst_n = [100, 200, 300, 300, 100]
lst_m = [500, 100, 100, 200, 100]
s = 1000 # 1000

n = 5
m = 5

# Матрица возможных исходов
matrix = []

# Заготовка - матрица пустышка размером m+1 на n+1
for i in range(n+1):
    matrix.append([0] * (m+1))

# Установка исходных стоимостей добраться до каждого резюме из стопкок в Матрицу возможных исходов

# Заполнение строки матрицы
for i in range(n):
    matrix[0][i+1] = sum(lst_n[:i+1])

# Заполнение столбца матрицы
for i in range(1, m+1):
    matrix[i][0] = sum(lst_m[:i])


# output full matrix template
for row in matrix:
    print(row, sep='\n')

# Определяю, в каком диапозоне матрицы имеет смысл вести поиск.
# Т.е. в пределах каких строк и столбцов можно искать ответ с заданным бюджетом
i_max = 0
j_max = 0

# Максимальный индекс столбца
for ind, el in enumerate(matrix[0]):
    if s >= el:
        j_max = ind

# Максимальный индекс строки
for i in range(m+1):
    if s >= matrix[i][0]:
        i_max = i

# Иду по строкам матрицы возможных исходов, 
# чтобы определить макс. кол. резюме, что можно собрать
max_cv_collected = 0
# Для рассчёта стоимости взятия резюме, соответствующих индексам i j
# Использую непосредственные стоимости этих резюме.

# Добавляю 0, чтобы размерности совпали с представлением матрицы
lst_n.insert(0, 0) 
lst_m.insert(0, 0) 


# алгоритм рассчёта стоимости взятия резюме, соответствующих индексам i j
for i in range(0, i_max+1):
    for j in range(1, j_max+1):
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

print(max_cv_collected)
