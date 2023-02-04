import bisect

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    m = int(input().strip())
    a.sort()
    for i in range(m):
        k = int(input().strip())
        ans = bisect.bisect_right(a, k)
        print(ans)

if __name__ == '__main__':
    main()