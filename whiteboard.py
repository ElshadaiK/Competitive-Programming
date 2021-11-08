def eraser(n):
    last = n
    prev = n - 1
    print(2)
    for i in range(n-1):
        print(last, prev)
        if(last+prev)%2 == 0:
            last = (last+prev)//2
        else:
            last = (last+prev)//2 + 1
        prev -= 1

if __name__ == '__main__':
    t = int(input().rstrip())
    output = []
    for i in range(t):
        first_in = int(input().rstrip())
        output.append(first_in)
    for items in output:
        eraser(items)
    