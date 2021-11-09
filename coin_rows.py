from collections import deque


def collector(values, total):
    prefix_sum = [[values[0][0]], [values[1][0]]]
    for i in range(len(values)):
        for j in range(1, len(values[i])):
            prefix_sum[i].append(prefix_sum[i][-1] + values[i][j])
    alice = dfs(values, 0, 0, prefix_sum) 

    return alice
    

def dfs(values, i, j, prefix_sum):
    q = deque([(i,j)])

    while(q):
        i, j = q.popleft()

        if(i == 1 or j == len(values[0])-1):
            op1 = prefix_sum[0][-1] - prefix_sum[0][j]
            op2 = prefix_sum[1][j] - values[1][j]
            res = max(op1, op2)
            return res
        
        op1 = prefix_sum[0][-1] - prefix_sum[0][j]
        op2 = prefix_sum[1][j]
        
        if(op1 > op2):
            q.append((i, j+1))
        else:
            q.append((i, j+1))
            return dfs(values, i+1, j, prefix_sum)

def dfsR(values, i, j, prefix_sum):
    if(i == 1 or j == len(values[0])-1):
        op1 = prefix_sum[0][-1] - prefix_sum[0][j]
        op2 = prefix_sum[1][j] - values[1][j]
        res = max(op1, op2)
        return res
    
    op1 = prefix_sum[0][-1] - prefix_sum[0][j]
    op2 = prefix_sum[1][j]
    
    if(op1 > op2):
        return dfs(values, i, j+1, prefix_sum)
    else:
        return dfs(values, i+1, j, prefix_sum)
    
if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    res = []
    for i in range(t):
        n = int(input().rstrip())
        first_input = input().rstrip().split()
        second_input = input().rstrip().split()
        total  = 0
        output = [[],[]]
        for k in range(n):
            output[0].append(int(first_input[k]))
            total += int(first_input[k])
        for k in range(n):
            output[1].append(int(second_input[k]))
            total += int(second_input[k])
        temp.append([n, output, total])
    for items in temp:
        print(collector(items[1], items[2]))