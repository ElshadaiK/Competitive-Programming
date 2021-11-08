def moves(r1,c1, r2,c2):
    rook = 0
    bishop = 0
    king = 0
    rdiff = abs(r1 - r2)
    cdiff = abs(c1 - c2)
    if rdiff:
        rook += 1
    if cdiff:
        rook += 1
    slope1 = abs(c1-r1)
    slope2 = abs(c2-r2)
    if(slope1 == slope2):
        bishop = 1
    elif cdiff == rdiff:
        bishop = 1

    else:
        if(r1 == r2 or c1 == c2):
            if(r1 == r2 and cdiff % 2 == 1):
                bishop = 0
            elif(c1 == c2 and rdiff % 2 == 1):
                bishop = 0
            else:
                bishop = 2
        else:
            bishop = 2
    while(abs(r1-r2) != abs(c1-c2)):
        if(c1 < c2):
            c1 += 1
            king += 1
        elif(c1 > c2):
            c1 -= 1
            king += 1
        if(r1 < r2):
            r1 += 1
            king += 1
        elif(r1 > r2):
            r1 -= 1
            king += 1
    if(slope1 == slope2):
        king += abs(c1-c2)
    print(rook, bishop, king)

if __name__ == '__main__':
    n = input().rstrip().split()
    moves(int(n[0]), int(n[1]), int(n[2]), int(n[3]))