def sorter(arr):
    holder = [0]*100
    result = []
    for i in range(len(arr)):
        holder[arr[i]] += 1
    for j in range(len(holder)):
        if(holder[j] != 0):
            for k in range(holder[j]):
                result.append(j)
    return result

print(sorter([8,2,4,7,9,1,2,5,7,9,4]))