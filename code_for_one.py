def coder(n, l, r):
    ans = []
    res = calculator(n, ans)
    print(ans)

def calculator(n, ans):
    if(n == 1 or n == 0):
        return n
    else:
        middle = 0
        if(n%2 == 1):
            middle = 1
        side = calculator(n//2, ans)
        ans.append(side)
        ans.append(middle)
        ans.append(side)


coder(7,0,0)