# n - строки m - столбцы
n, m = map(int, input().split())

matrix = []

for _ in range(m):
    matrix.append(list(map(int, input().split())))

# input 1
'''
5 4
0 1 1 0 0
1 1 1 0 1
1 1 0 0 1
0 0 0 1 0
'''
# print(*matrix, sep='\n')

# TODO: Как досрочно завершать работу функции, если регион распознан?
# TODO: Как искать вложенные регионы? Это нужно, т.к. покупка вложенного региона быть выгоднее!
def find_region(matrix: list, i: int, j: int): # Координата, начиная с которой следует запускать поиск
    def update_end_point():
        pass
    
    region_coords = [['i_start', 'j_start'], ['i_end', 'j_end']] # [['i', 'j'], ['i', 'j']]
    for y in range(i, n): # по строкам
        for x in range(j, m): # по столбцам
            if matrix[y][x]:
                if region_coords[0][0] == 'i_start': # Если начальная точка региона не определена
                    region_coords[0][0] = x
                    region_coords[0][1] = y
                    region_coords[1][0] = x
                    region_coords[1][1] = y
                elif region_coords[1][0] == x-1 and region_coords[1][1] == y:
                    region_coords[1][0] = x
                    region_coords[1][1] = y
                    pass

def estimate_region(matrix: list, lst: list): # lst - список списков координат региона
    pass


def get_best_region_area(marks: list): # Принимает список списков полных оценок регионов
    if marks:
        return marks[0][1] # Площадь лучшего
    return 0 # отказ от покупки

regions = []

# Одно целое число, площадь наилучшего региона, или 0, в случае отказа от покупки
print("0")
