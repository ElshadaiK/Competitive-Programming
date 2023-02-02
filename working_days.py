def calculate(n):
    res = 0
    print((n-6)//3)
if __name__ == '__main__':
    t = int(input().rstrip())
    store = []
    for i in range(t):
        n = int(input().rstrip())
        store.append(n)
    for items in store:
        calculate(items)