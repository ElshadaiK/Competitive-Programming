def games(n, k):
    temp = n*(n-1)/2 
    temp = temp - n*k
    if(temp < 0):
        print(-1)
    else:
        print(k * n)

        for i in range(1, n):
            j = i+1
            count = 0
            while count < k:
                if(j > n):
                    j -= n
                print(i, j)
                count += 1
                j += 1
        count = 0
        i = 1
        while count < k:
            print(n, i)
            count += 1
            i += 1

            
if __name__ == '__main__':
    inp = input().rstrip().split()
    n = int(inp[0])
    k = int(inp[1])
    games(n, k)