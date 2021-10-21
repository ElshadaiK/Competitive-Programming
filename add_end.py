def addend(num):
    n = 0
    while(int(num) > 1):
        possibles = []
        possibles.append(len(num)*"1")
        if(len(num) > 1):
            possibles.append((len(num)-1)*"1")
        possibles.append((len(num)+1)*"1")
        minimum = int(num)
        for possible in possibles:
            x = int(num) - int(possible)
            if(abs(x) < minimum):
                h = len(possible)
                minimum = abs(x)
        n += h
        num = str(minimum)
    if(int(num) == 1):
        n += 1
    return n

def reader():
    n = input()
    print(addend(n))

reader()