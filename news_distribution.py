def distribution(lst):
    checked = set()
    visited = {}
    coll = lst[1]
    for i in range(1, lst[0][0]+1):
        if(i not in visited):
            visited[i] = helper(coll, i)
def dfs(visited, ):
    for key in visited:
        visited.add(key)
        temp = visited[key]
        for i in temp:
            if(i not in checked):
                
    print(visited)
    return 0

def helper(lst, ptr):
    res = set()
    for items in lst:
        if(ptr in items):
            for item in items:
                res.add(item)
    return res

distribution([
    (7, 5),
    [[2, 5, 4],
    [],
    [1, 2],
    [1],
    [6, 7]]
])