def walker(n, k, available):
    sum_walks = []
    counter = 0
    for i in range(1, len(available)):
        sum_walks.append(available[i] + available[i-1])
    available_cop = available[:]
    for i in range(len(sum_walks)):
        if(sum_walks[i] < k):
            if(i < len(sum_walks)-1):
                if(sum_walks[i+1] < k):
                    temp = k - sum_walks[i]
                    available_cop[i+1] += temp
                    sum_walks[i] += temp
                    sum_walks[i+1] += temp
                    counter += temp
                else:
                    temp = k - sum_walks[i]
                    available_cop[i] += temp
                    sum_walks[i] += temp
                    counter += temp
            else:
                temp = k - sum_walks[i]
                available_cop[i+1] += temp
                sum_walks[i] += temp
                counter += temp
    print(counter)
    res = ""
    for i in available_cop:
        res += str(i) + " "
    print(res)

if __name__ == '__main__':
    inp = input().rstrip().split()
    n = int(inp[0])
    k = int(inp[1])
    nums = input().rstrip().split()
    for i in range(n):
        nums[i] = (int(nums[i]))
    walker(n, k, nums)