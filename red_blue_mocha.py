def assigner(n, word):
    res = ""
    store = {}
    indexes = set()
    for i in range(len(word)):
        if(word[i] != '?'):
            store[i] = word[i]
            indexes.add(i)
    if(len(indexes) == n):
        return word
    elif(len(indexes) == 0):
        isB = True
        for i in range(n):
            if(isB):
                res += "B"
            else:
                res += "R"
            isB = not isB
        return res
    for index in indexes:
        temp = index -1
        nex = index
        while(temp >= 0 and temp not in store):
            if store[nex] == 'B':
                store[temp] = "R"
            else:
                store[temp] = "B"

            temp -= 1
            nex -= 1
    ptr = max(store) + 1
    last = store[ptr-1]
    while(ptr != n):
        if(last == "B"):
            store[ptr] = 'R'
            last = "R"
        else:
            store[ptr] = 'B'
            last = "B"
        ptr += 1
        
    for i in range(n):
        res += store[i]

    return res

if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    for i in range(t):
        n = int(input().rstrip())
        word = input().rstrip()
        temp.append([n, word])
    for items in temp:
        print(assigner(items[0], items[1]))

