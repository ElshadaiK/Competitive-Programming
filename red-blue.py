def chooser(n, r, b):
    blue = 0
    red = 0
    for i in range(n):
        if(r[i] > b[i]):
            red += 1
        elif(b[i] > r[i]):
            blue += 1
    if(red == blue):
        return "EQUAL"
    elif(red > blue):
        return "RED"
    else:
        return "BLUE"

if __name__ == '__main__':
    t = int(input().rstrip())
    holder = []
    for i in range(t):
        n = int(input().rstrip())
        r = input().rstrip()
        b = input().rstrip()
        holder.append([n, r, b])

    for elem in holder:
        print(chooser(elem[0], elem[1], elem[2]))