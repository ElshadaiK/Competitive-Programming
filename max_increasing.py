def solution(arr):
    glob_count = 0
    count = 1
    for i in range(1, len(arr)):
        if(arr[i] > arr[i-1]):
            count += 1
        else:
            glob_count = max(glob_count, count)
            count = 1
    glob_count = max(glob_count, count)
    return glob_count

if __name__ == '__main__':
    n = int(input().rstrip())
    nums = input().rstrip().split()
    for i in range(n):
        nums[i] = (int(nums[i]))
    print(solution(nums))