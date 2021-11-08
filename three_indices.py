def indexer(listnum):
    store = []
    first = False
    second = False
    temp = 0
    mini = 0
    
    for j in range(len(listnum)):
        if(store):
            if(not first):
                mini =  min(store)
                if(listnum[j] > mini):
                    first = True
                    holder = []
                    holder.append(listnum.index(mini))
                    holder.append(j)
                    temp = listnum[j]
                store.append(listnum[j])
            else:
                if(listnum[j] < temp):
                    second = True
                    holder.append(j)
                else:
                    temp = listnum[j]
                    holder.pop()
                    holder.append(j)
                store.append(listnum[j])
        else:
            store.append(listnum[j])
        if(first and second):
            print("YES")
            res = ""
            for item in holder:
                res += str(item+1) + " "
            return res
    return "NO"
    
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
        print(indexer(items[1]))