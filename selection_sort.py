def sorter(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
             if(arr[mini] > arr[j]):
                 mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

print(sorter([8,2,4,7,9,1,2,5,7,9,4]))