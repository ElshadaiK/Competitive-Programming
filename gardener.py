def gardener(n, k, listr):
    if(n <= k):
        return 0
    adj_lst = {}
    for edge in listr:
        edge = edge.split(' ')
        i = edge[0]
        j = edge[1]
        if(i not in adj_lst):
            adj_lst[i] = set()
        if(j not in adj_lst):
            adj_lst[j] = set()
        adj_lst[i].add(j)
        adj_lst[j].add(i)
    m = n
    while(k and adj_lst):
        removed = set()
        empty = set()

        for key in adj_lst:
            val = adj_lst[key]
            if(len(val) == 1):
                popped = val.pop()
                removed.add((popped, key))
                empty.add(key)
            elif(len(val) == 0):
                empty.add(key)
        for elem in empty:
            m -= 1
            del adj_lst[elem]

        for elem in removed:
            if(elem[0] in adj_lst):
                if(elem[1] in adj_lst[elem[0]]):
                    adj_lst[elem[0]].remove(elem[1])
            
                
        k -= 1

    return m

if __name__ == '__main__':
    t = int(input().rstrip())
    newline = input().rstrip()
    res = []
    for i in range(t):
        output = []
        first_input = input().rstrip().split(' ')
        n = int(first_input[0])
        k = int(first_input[1])
        for j in range(n-1):
            edges = input().rstrip()
            output.append(edges)
        if(i != t-1):
            newline = input().rstrip()
        res.append([n,k,output])
    for result in res:
        print(gardener(result[0], result[1], result[2]))