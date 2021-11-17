import math
inp = (input().rstrip().split())
a = int(inp[0])
b = int(inp[1])


def joysticker(a, b):
    count = 0
    while(a > 0 and b > 0):
        if(a == 1 and b==1):
            break
        if(a>b):
            b += 1
            a -= 2
        else:
            a += 1
            b -= 2
        count += 1
    return count



print(joysticker(a,b))