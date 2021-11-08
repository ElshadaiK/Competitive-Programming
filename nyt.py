def tranporter(n, t, lst):
    i = 0
    while(i<t-1):
        i = i + lst[i]
    if(i == t-1):
        return "YES"
    return "NO"

if __name__ == '__main__':
    n = (input().rstrip()).split()
    t = int(n[1])
    n = int(n[0])
    output = []
    first_input = (input().rstrip()).split()
    for i in range(n-1):
        output.append(int(first_input[i]))

    print(tranporter(n, t, output))