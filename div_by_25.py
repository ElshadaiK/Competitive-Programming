def solution(nums):
    count = 0
    if(int(nums)%25 == 0):
        return count
    else:
        i = len(nums) -1
        divs = {}
        removal = 0
        while i > -1:
            if(nums[i] == '0'):
                if(0 in divs):
                    removal -= 1
                    return removal
                else:
                    divs[0] = i
                    removal += 1
            elif(nums[i] == '5'):
                if(0 in divs):
                    removal -= 1
                    return removal
                else:
                    divs[5] = i
                    removal += 1
            elif(nums[i] == '2'):
                if(5 in divs):
                    removal -= 1
                    return removal
                else:
                    removal += 1

            elif(nums[i] == '7'):
                if(5 in divs):
                    removal -= 1
                    return removal
                else:
                    removal += 1
            else:
                removal += 1
            i -= 1


def reader():
    n = int(input())
    lst=[]
    for i in range(n):
        nums = input()
        lst.append(nums)
    for nums in lst:
        print(solution(nums))

reader()
