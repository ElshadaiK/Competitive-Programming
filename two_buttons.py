from collections import deque
def solution(n, m):
    minimum = 0
    q = deque([])
    visted = {}
    q.append((n,0))
    while(q):
        curr_n, curr_count = q.popleft()
        visted[curr_n] = curr_count
        if(curr_n > m):
            if(curr_n-1 not in visted):
                q.append((curr_n-1, curr_count+1))
        elif(curr_n == m):
            minimum = curr_count
            break
        else:
            if(curr_n-1 not in visted):
                q.append((curr_n-1, curr_count+1))
            if(curr_n*2 not in visted):
                q.append((curr_n*2, curr_count+1))

    return minimum


inp = (input().rstrip().split())
a = int(inp[0])
b = int(inp[1])

print(solution(a,b))