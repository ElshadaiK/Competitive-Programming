def relativeSortArray(arr1, arr2):
    result = arr2.copy()
    for i in range(len(arr1)):
        if(arr1[i] in arr2):
            ind = result.index(arr1[i])
            result.insert(ind, arr1[i])
        else:
            ind = result.index(arr2[-1]) +1
            final = len(result) -1
            if(ind == final):
                result.append(arr1[i])
            else:
                found = False
                for j in range(ind+1, final+1):
                    if(result[j] >= arr1[i]):
                        result.insert(j, arr1[i])
                        found = True
                        break
                if(not found):
                    result.append(arr1[i])
    for i in range(len(arr2)):
        result.remove(arr2[i])
    return result