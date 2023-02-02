def solution(n, m, grid):
    res = ""
    store = dict()
    for i in range(n):
        for j in range(m):
            if((i,j)) not in store: store[(i,j)] = set()
            store[(i,j)].add(grid[i][j])
    print(store)
    return res

if __name__ == '__main__':
    t = (input().rstrip()).split(" ")
    n = int(t[0])
    m = int(t[1])
    grid = []
    for _ in range(n):
        grid.append(list(input().rstrip()))
    print(solution(n, m, grid))