def solution(n, b, w):
    cnt = 0
    for p in range(n):
        if(w[p] == '0'):
            continue
        if(p > 0 and b[p - 1] == '1'):
            b[p - 1] = 'x'
            cnt += 1
        elif(b[p] == '0'):
            b[p] = 'x'
            cnt += 1
        elif(p + 1 < n and b[p + 1] == '1'):
            b[p + 1] = 'x' 
            cnt += 1
    return cnt

if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    for i in range(t):
        n = int(input().rstrip())
        str1 = list(input().rstrip())
        str2 = list(input().rstrip())
        temp.append([n, str1, str2])
    for items in temp:
        print(solution(items[0], items[1], items[2]))