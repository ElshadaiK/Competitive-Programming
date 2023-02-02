def calculate(n, a):
    a.sort()
    v = []
    for i in range(n):
        if i >= a[i]:
            v.append('t')
        else:
            v.append('f')
    ans = 0
    for i in range(n):
        if v[i] == 't':
            if i == 0:
                ans += 1
            elif v[i-1] == 'f':
                ans += 1
    if a[0] != 0:
        ans += 1
    print(ans)
if __name__ == '__main__':
    t = int(input().rstrip())
    store = []
    for i in range(t):
        n = int(input().rstrip())
        a = input().rstrip().split(' ')
        store.append([n, [int(x) for x in a]])
    for items in store:
        calculate(items[0], items[1])