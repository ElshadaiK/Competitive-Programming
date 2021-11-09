def maximizer(reds, blues):
    red_sum = 0
    blue_sum = 0

    max_red = 0
    max_blue = 0

    for red in reds:
        red_sum += int(red)
        max_red = max(max_red, red_sum)
    for blue in blues:
        blue_sum += int(blue)
        max_blue = max(max_blue, blue_sum)

    return max_blue+max_red


if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    for i in range(t):
        red_count = int(input().rstrip())
        reds = input().rstrip().split()
        blue_count = int(input().rstrip())
        
        blues = input().rstrip().split()
        temp.append([reds, blues])

    for inputs in temp:
        print(maximizer(inputs[0], inputs[1]))