def jumper(string):
    longest = 1
    counter = 1
    for i in range(len(string)):
        
        if(string[i] == 'L'):
            counter += 1
        else:
            longest = max(longest, counter)
            counter = 1
            
    longest = max(longest, counter)

    return longest

if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    for i in range(t):
        string = (input().rstrip())
        temp.append(string)
    for item in temp:
        print(jumper(item))