def solution(n, k, lst):
    doubles = []
    cakes = []
    temp = set()
    for i in range(1, len(lst)):
        if(lst[i] == lst[i-1]):
            doubles.append(i)
            cakes.append(len(temp))
            temp = set()
            temp.add(i)
        else:
            if(lst[i] not in temp):
                temp.add(lst[i])
    cakes.append(len(temp))
    if(k == len(cakes)):
        print(sum(cakes))
    elif(k < len(cakes)):
        print("lol")
    else:
        print("lmao")
    print(k, doubles, cakes)
    return 0

def reader():
    n_and_k = input().split(" ")
    n = int(n_and_k[0])
    k = int(n_and_k[1])
    nums = input().split(' ')
    lst=[]
    for i in nums:
        lst.append(int(i))
    solution(n, k, lst)

reader()