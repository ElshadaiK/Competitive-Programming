def findBug(n):
    if(n <= 2):
        return -1
    res = ""
    for i in range(n, 0, -1):
        res += str(i) + " "
    return res

if __name__ == '__main__':
    n = int(input().rstrip())
    
    print(findBug(n))