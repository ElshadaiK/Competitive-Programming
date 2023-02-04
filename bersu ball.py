def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    m = int(input().strip())
    b = list(map(int, input().strip().split()))
    a.sort()
    b.sort()

    pairs = 0
    for i in range(n):
        for j in range(m):
            if abs(a[i] - b[j]) < 2:
                b[j] = 1000
                pairs += 1
                break

    print(pairs)

if __name__ == '__main__':
    main()
