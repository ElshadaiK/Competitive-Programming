n = input().rstrip().split()
w = int(n[0])
h = int(n[1])
ans = (2**(w+h))%998244353 
print(ans)