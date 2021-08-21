def findMedian(arr):
    # Write your code here
    if(len(arr) == 1):
        return arr[0]
    
    items = [0]*20002
    for i in range(len(arr)):
        items[arr[i] + 10000] += 1
    count = 0
    result = 0
    ptr = 0
    for i in range(len(items)):
        if(items[i] != 0):
            if(count < (len(arr)//2)):
                count += items[i]
                ptr = i
            elif(count == (len(arr)//2)):
                result = i-10000
                break
            else:
                result = ptr-10000
                break
    return result