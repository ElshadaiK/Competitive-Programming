def calculate(n, m):
    temp = n+m-2
    res = "Tonya" if temp%2==0 else "Burenka"
    print(res)
if __name__ == '__main__':
    t = int(input().rstrip())
    store = []
    for i in range(t):
        n = input().rstrip().split(' ')
        store.append([int(n[0]), int(n[1])])
    for items in store:
        calculate(items[0], items[1])