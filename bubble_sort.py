def sorter(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-1-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr

print(sorter([8,2,4,7,9,1,2,5,7,9,4]))