def jumper(arr):
    store = {}
    maxim = 0
    for i in range(len(arr)):
        potential = dfs(i, arr, store)
        
        maxim = max(maxim, potential)
    return maxim

def dfs(j, arr, store):
    if(j < len(arr)):
        if(arr[j] not in store):
            store[j] = arr[j] + dfs(arr[j]+j, arr, store)
        return store[arr[j]]
    else:
        return 0

if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    res = []
    for i in range(t):
        n = int(input().rstrip())
        first_input = input().rstrip().split()
        
        output = []
        for k in range(n):
            output.append(int(first_input[k]))
        temp.append([n, output])
    for items in temp:
        print(jumper(items[1]))