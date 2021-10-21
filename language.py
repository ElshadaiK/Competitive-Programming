def solution(inp):
    count = 0
    vs = []
    for i in range(len(inp)):
        if inp[i] == "w":
            count += 1
        elif inp[i] == 'v':
            if(vs != []):
                if(i-1 == vs[-1]):
                    count += 1
                    vs.pop()
                else:
                    vs.append(i)
            else:
                vs.append(i)
    return count

def reader():
    n = int(input())
    lst=[]
    for _ in range(n):
        letters = input()
        lst.append(letters)
    for letters in lst:
        print(solution(letters))

reader()
