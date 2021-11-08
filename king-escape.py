def escapes(n, ax, ay, bx, by, cx, cy):
    horizontally = True
    vertically = True
    if(ax in range(min(cx,bx), max(cx,bx))):
        horizontally = False
    if(ay in range(min(cy,by), max(cy,by))):
        vertically = False
    if(horizontally and vertically):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    n = int(input().rstrip())
    a = input().rstrip().split()
    b = input().rstrip().split()
    c = input().rstrip().split()

    print(escapes(n, int(a[0]), int(a[1]), int(b[0]), int(b[1]), int(c[0]), int(c[1])))