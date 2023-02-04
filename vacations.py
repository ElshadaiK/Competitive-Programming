def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    dp = [[0] * 3 for i in range(n)]
    if a[0] == 1 or a[0] == 3:
        dp[0][1] += 1
    if a[0] == 2 or a[0] == 3:
        dp[0][2] += 1
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], max(dp[i-1][1], dp[i-1][2]))
        dp[i][1] = max(dp[i-1][0], dp[i-1][2])
        if a[i] == 1 or a[i] == 3:
            dp[i][1] += 1
        dp[i][2] = max(dp[i-1][0], dp[i-1][1])
        if a[i] == 2 or a[i] == 3:
            dp[i][2] += 1
    print(n - max(dp[n-1][0], max(dp[n-1][1], dp[n-1][2])))

if __name__ == '__main__':
    main()