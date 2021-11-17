def namer(arrnames):
    store = {}
    for names in arrnames:
        start = names[0]
        end = names[1]
        if(start not in store):
            store[end] = start
        else:
            store[end] = store[start]
            del store[start]
    print(len(store))
    for key in store:
        print(store[key], " ", key)

if __name__ == '__main__':
    n = int(input().rstrip())
    temp = []
    for i in range(n):
        first_input = input().rstrip().split()
        temp.append(first_input)
    (namer(temp))