def oner(nums):
    negs = 0
    zero = 0
    count = 0
    for i in nums:
        if(i < 0):
            negs += 1
            count +=  -1 + abs(i)
        elif(i == 0):
            zero += 1
            count += 1
        else:
            count +=  i - 1
        
    if(negs%2 == 1 and zero == 0):
        count += 2
    return count

if __name__ == '__main__':
    n = int(input().rstrip())
    nums = input().rstrip().split()
    for i in range(n):
        nums[i] = (int(nums[i]))
    print(oner(nums))
