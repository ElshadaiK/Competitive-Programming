def pairing(n, l, r, listnum):
    total  = n*(n-1)/2

if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    res = []
    for i in range(t):
        first_input = input().rstrip().split()
        n = int(first_input[0])
        l = int(first_input[1])
        r = int(first_input[2])
        second_input = input().rstrip().split()
        output = []
        for k in range(n):
            output.append(int(second_input[k]))
        temp.append([n, l, r, output])
    for items in temp:
        print(pairing(items[0], items[1], items[2], items[3]))