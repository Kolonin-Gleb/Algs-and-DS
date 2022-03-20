from collections import deque

def bfs(graph, start):
    visited=[]
    visited.append(start)
    queue=deque()
    queue.append(start)
    while queue:
        cur=queue[0]
        queue.popleft()
        for u in graph[cur]:
            if u not in visited:
                visited.append(u)
                queue.append(u)
    return print(queue)


def bfs_dist(graph, start):
    dist={}
    for v in graph:
        dist[v]=0
    visited=[]
    visited.append(start)
    queue=deque()
    queue.append(start)
    while queue:
        cur=queue[0]
        queue.popleft()
        for u in graph[cur]:
            if u not in visited:
                visited.append(u)
                queue.append(u)
                dist[u]+=dist[cur]+1
                
    return dist


# def bfs_con_component(graph, start,cnt=0):
#     visited=[]
#     visited.append(start)
#     queue=deque()
#     queue.append(start)
#     while queue:
#         cur=queue[0]
#         queue.popleft()
#         for u in graph[cur]:
#             if u not in visited:
#                 visited.append(u)
#                 queue.append(u)

#     return print(queue)

def bfs_parent(graph, start):
    parent={}
    for v in graph:
        parent[v]=None
    visited=[]
    visited.append(start)
    queue=deque()
    queue.append(start)
    while queue:
        cur=queue[0]
        queue.popleft()
        for u in graph[cur]:
            if u not in visited:
                visited.append(u)
                queue.append(u)
                parent[u]=cur
                
    return parent

def path(graph, start,end):
    parents=bfs_parent(graph,start)
    p=[]
    p.append(end)
    while start not in p:
        par=parents[end]
        p.append(par)
        end=par
    return print(p[::-1])
        
def vertex_on_path(graph, start, end, x):
    start_dist=bfs_dist(graph,start)
    end_dist=bfs_dist(graph,end)
    if start_dist[x]+end_dist[x]==start_dist[end]:
        print('Vertex is on the shortest path')
    else:
        print('Vertex is not on the shortest path')
        
def edge_on_path(graph, start, end, edge):
    start_dist=bfs_dist(graph,start)
    end_dist=bfs_dist(graph,end)
    if start_dist[edge[0]]+end_dist[edge[1]]+1==start_dist[end]:
        print('The edge is on the shortest path')
    else:
        print('The edge is not on the shortest path')
        
gr = {
    'A':['B'],
    'B':['A','C', 'D'],
    'C':['B','D','E'],
    'D':['B', 'C'],
    'E':['C']
}

# print(bfs(gr,'A'))
# print(bfs_dist(gr,'A'))
print(bfs_parent(gr,'A'))
# print(path(gr,'A','E'))
# print(vertex_on_path(gr,'A','E', 'B'))
# print(edge_on_path(gr,'A','E', 'BC'))
