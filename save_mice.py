def saver(n, mice):
    count = 0
    diff = []
    for mouse in mice:
        i = n - mouse
        diff.append(i)
    diff.sort()
    prefix_sum = 0
    for i in range(len(diff)):
        if(diff[i] + prefix_sum) < n:
            prefix_sum += diff[i]
            count += 1
        if(prefix_sum == n):
            break

    return count

if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    for i in range(t):
        first_input = input().rstrip().split()
        n = int(first_input[0])
        k = int(first_input[1])
        second_input = input().rstrip().split()
        
        for j in range(k):
            second_input[j] = int(second_input[j])
        temp.append([n, k, second_input])
    for items in temp:
        print(saver(items[0], items[2]))
