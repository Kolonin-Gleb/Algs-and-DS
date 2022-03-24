from collections import deque

G = {
    'A':{'B':5, 'C':15, 'D':10},
    'B':{'D':2, 'F':11},
    'C':{'D':4, 'E':6},
    'D':{'A':3, 'C':3, 'E':5, 'F':4},
    'E':{'C':2, 'F':6},
    'F':{'E':2},
}

def deikstra (start_vertex, G):

    distances = {} # расстояние от начальной вершины
    distances[start_vertex] = 0

    queue = deque()
    queue.append(start_vertex)

    while queue:
        cur_vertex = queue.popleft()

        for neighbor in G[cur_vertex]:
            if (neighbor not in distances
                or distances[cur_vertex] + G[cur_vertex][neighbor] < distances[neighbor]):
                distances[neighbor] = distances[cur_vertex] + G[cur_vertex][neighbor]
                queue.append(neighbor)
    return distances

print(deikstra('E', G))




