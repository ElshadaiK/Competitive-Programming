def decorator(r, g, b):
    count = 0
    ordered = sorted([r,g,b])
    count += ordered[0]
    if(ordered[1] > ordered[0]):
        diff1 = ordered[1]-ordered[0]
        diff2 = ordered[2]-ordered[0]

        div1 = diff1//3
        div2 = diff2//3
        rem1 = diff1%3
        rem2 = diff2%3
        if(diff2 == 1):
            return count
        if(div1 + div2 > ordered[1]):
            if(rem1 + rem2 == 3):
                return count + ordered[1] + 1
            return count+ordered[1]
        if(rem1 + rem2 == 3):
            count += div1 + div2 + 1
        else:
            count += div1 + div2 

    return count

inp = (input().rstrip().split())
r = int(inp[0])
g = int(inp[1])
b = int(inp[2])

print(decorator(r,g,b))

500000000 
1000000000 
500000000