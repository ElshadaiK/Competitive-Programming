def solution(n, m, poland, enemy):
    common = set()
    for word in poland:
        if word in enemy: common.add(word)
    if n+m-len(common)>0:
        com=n+m-len(common)
        n-=com
        m-=com
        
        if(com%2==1):
            n+=(com)/2+1
            m+=(com)/2
        else:
            n+=(com)/2
            m+=(com)/2

        if(n>m):
            return("YES")
        else:
            return("NO")

if __name__ == '__main__':
    t = (input().rstrip()).split(" ")
    n = int(t[0])
    m = int(t[1])
    poland = set()
    enemy = set()
    for _ in range(n):
        poland.add(input().rstrip())
    for _ in range(m):
        enemy.add(input().rstrip())
    print(solution(n, m, poland, enemy))