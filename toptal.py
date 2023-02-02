def getChange(M, P):
    result = {
        0.01: 0,
        0.05: 0,
        0.1: 0,
        0.25: 0,
        0.5: 0,
        1: 0
    }
    ret = M - P
    while(ret > 0):
        print(ret)
        if(ret >= 1):
            div = 1
        elif(ret >= 0.5):
            div = 0.5
        elif(ret >= 0.25):
            div = 0.25
        elif(ret >= 0.1):
            div = 0.1
        elif(ret >= 0.05):
            div = 0.05
        elif(ret >= 0.01):
            div = 0.01
        temp = ret//div
        ret -= temp
        result[div] += temp
    ans = []
    for key in result:
        ans.append(result[key])
    
    return ans

print(getChange(5,0.99))
# getChange(5, 0.99) 
# # should return [1,0,0,0,0,4]

# getChange(3.14, 1.99) 
# # should return [0,1,1,0,0,1]
# getChange(3, 0.01) 
# # should return [4,0,2,1,1,2]
# getChange(4, 3.14) 
# # should return [1,0,1,1,1,0]
# getChange(0.45, 0.34) # should return [1,0,1,0,0,0]