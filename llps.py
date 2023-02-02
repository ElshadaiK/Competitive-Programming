def solution(inp):
    res = ""
    flag = False
    a = [0]*30
    for i in range(len(inp)):
        a[ord(inp[i])-ord('a')] += 1
    j = 27
    while j >= 0:
        if(a[j]>0 and not flag):
            while(a[j] > 0):
                res += (chr(j + ord('a'))) 
                a[j] -= 1
                flag= True
        j -= 1
    return res
        
if __name__ == '__main__':
    inp = input().rstrip()
    print(solution(inp))

