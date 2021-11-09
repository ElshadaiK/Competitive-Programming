def maximizer(inp, letters):
    prefix_sum = [inp[0]]

    for i in range(1, len(inp)):
        prefix_sum.append(prefix_sum[i-1] + inp[i])

    ptr = 0

    for letter in letters:
        while(letter > prefix_sum[ptr]):
            ptr += 1

        dormitory = ptr+1
        room = 0
        if(ptr == 0):
            room = letter
        else:
            room =  letter - prefix_sum[ptr-1] 

        print(dormitory, room)


if __name__ == '__main__':
    inp = (input().rstrip()).split()
    n = int(inp[0])
    m = int(inp[1])
    dormitories = input().rstrip().split()
    rooms = input().rstrip().split()
    for i in range(n):
        dormitories[i] = int(dormitories[i])
    for i in range(m):
        rooms[i] = int(rooms[i])
    maximizer(dormitories, rooms)