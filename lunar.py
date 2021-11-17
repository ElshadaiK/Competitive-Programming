from collections import deque
def wanderer(edges):
    store = {}
    for edge in edges:
        if(edge[1] not in store):
            store[edge[1]] = set()
        if(edge[0] not in store):
            store[edge[0]] = set()
        store[edge[0]].add(edge[1])
        store[edge[1]].add(edge[0])
    for edge in store:
        store[edge] = sorted(store[edge])
    visited = set()
    visited.add(1)
    print(1, end=' ')
    dfs(store, visited, 1)
    print("")
    
def dfs(store, visited,start):
    for child in store[start]:
        if(child not in visited):
            print(child, end=' ')
            visited.add(child)
            dfs(store, visited, child)

if __name__ == '__main__':
    first_input = input().rstrip().split()
    n = int(first_input[0])
    m = int(first_input[1])
    edges = []
    for i in range(m):
        second_input = input().rstrip().split()
        
        for k in range(2):
            second_input[k] = int(second_input[k])
        edges.append(second_input)
    (wanderer(edges))