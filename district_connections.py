def solution(n, gangs):
    villages = [i for i in range(1, n+1)]
    visited = set()
    roads = []
    dfs(villages, gangs, visited, roads)
    if(len(roads) < len(gangs)-1):
        print("NO")
    else:
        print("YES")
        for road in roads:
            print(road[0], road[1])


def dfs(villages, gangs, visited, roads):
    for i in range(len(villages)):
        if(villages[i] not in visited):
            visited.add(villages[i])
            for j in range(len(villages)):
                if(villages[j] not in visited and gangs[i] != gangs[j]):
                    roads.append((villages[i], villages[j]))
                    dfs(villages, gangs, visited, roads)

def reader():
    n = int(input())
    lst=[]
    for _ in range(n):
        m = int(input())
        nums = input().split(' ')
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        lst.append([m, nums])
    for elements in lst:
        solution(elements[0], elements[1])

reader()