def combinator(a, b, c, m):
    max_m = (a  + b + c -3)
    min_m = max(a,b,c) - (a+b+c - max(a,b,c) - min(a,b,c)) - min(a,b,c) - 1
    if min_m <= m <= max_m:
        return "YES"
    return "NO"

if __name__ == '__main__':
    t = int(input().rstrip())
    holder = []
    for i in range(t):
        n = input().rstrip().split()
        a = int(n[0])
        b = int(n[1])
        c = int(n[2])
        m = int(n[3])
        
        holder.append([a, b, c, m])

    for elem in holder:
        print(combinator(elem[0], elem[1], elem[2], elem[3]))