def reorganizeString(s):
    barcodes = []
    answer = ""
    for i in s:
        barcodes.append(ord(i) - 97)
    d = {}
    for i in barcodes:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    x = []
    for a,b in d.items():
        x.append([a,b])
    i = 0
    result = [0]*len(barcodes)
    x = sorted(x,key=lambda v:v[1])
    while i <len(result):
        result[i] = x[-1][0]
        x[-1][1]-=1
        if x[-1][1]==0:
            x.pop()
        i+=2
    i=1
    while i <len(result):
        result[i] = x[-1][0]
        x[-1][1]-=1
        if x[-1][1]==0:
            x.pop()
        i+=2
    answer += chr(result[0]+97)
    for i in range(1, len(result)):
        if(result[i] != result[i-1]):
            answer += chr(result[i]+97)
        else:
            return ""
    return answer
    