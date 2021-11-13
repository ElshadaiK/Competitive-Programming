def calculator(n, k, nums):
    occurances = {}
    items = set()
    for num in nums:
        temp = k - (num%k)
        if((num%k) != 0):
            items.add(temp)
            if(temp not in occurances):
                occurances[temp] = 0
            else:
                occurances[temp] += 1
    
    m = 0
    maximum = 0
    while(len(items) > 0):
        maximum = (max(items) + 1) + m*k
        m += 1
        items = set()
        for key in occurances:
            if(occurances[key] > 0):
                occurances[key] -= 1
                items.add(key)
    
    return maximum

if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    for i in range(t):
        inp = input().rstrip().split()
        n = int(inp[0])
        k = int(inp[1])
        nums = input().rstrip().split()
        for i in range(n):
            nums[i] = (int(nums[i]))
        temp.append([n, k, nums])
    
    for items in temp:
        print(calculator(items[0], items[1], items[2]))
            
