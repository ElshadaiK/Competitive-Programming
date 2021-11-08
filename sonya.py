
def countSet(listr):
    # + 2323
    store = {}
    output = []
    for items in listr:
        opr = items[0]
        item = items[2:]
        if(opr == "+"):
            pattern = helper(item)
            if(int(pattern) not in store):
                store[int(pattern)] = 0
            store[int(pattern)] += 1
        elif(opr == "-"):
            pattern = helper(item)
            store[int(pattern)] -= 1
        else:
            pattern = item
            if(int(pattern) not in store):
                output.append(0)
            else:
                output.append(store[int(pattern)])
    for res in output:
        print(res)

def helper(item):
    pattern = ""
    for i in item:
        if(int(i)%2==1):
            pattern += "1"
        else:
            pattern += "0"
    return pattern

if __name__ == '__main__':
    n = int(input().rstrip())
    output = []
    for i in range(n):
        first_input = input().rstrip()
        output.append(first_input)

    countSet(output)
