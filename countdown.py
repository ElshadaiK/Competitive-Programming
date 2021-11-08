def countdown(n, numstr):
    counter = 0
    for i in range(len(numstr)):
        if(numstr[i] != '0'):
            counter += int(numstr[i])
            if(i != len(numstr)-1):
                counter += 1
    return counter

if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    for i in range(t):
        n = int(input().rstrip())
        num = input().rstrip()
        temp.append([n, num])
    for items in temp:
        print(countdown(items[0], items[1]))

