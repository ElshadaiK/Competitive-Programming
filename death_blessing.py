def calculate(n, a, b):
    summed = 0
    for i in range(n):
        summed += a[i] + b[i]
    print(summed - max(b))
if __name__ == '__main__':
    t = int(input().rstrip())
    store = []
    for i in range(t):
        n = int(input().rstrip())
        a = input().rstrip().split(' ')
        b = input().rstrip().split(' ')
        store.append([n, [int(x) for x in a], [int(j) for j in b]])
    for items in store:
        calculate(items[0], items[1], items[2])