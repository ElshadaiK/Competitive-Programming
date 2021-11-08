import math
def chooser(men, women, team):
    ways = 0
    initial_men = 4
    initial_women = team - initial_men
    if(initial_women > women):
        initial_women = women
        initial_men = team - initial_women
    while(initial_women >= 1):
        tempMen = int(math.factorial(men)/(math.factorial(men-initial_men) * math.factorial(initial_men)))
        tempWomen = int(math.factorial(women)/(math.factorial(women-initial_women) * math.factorial(initial_women)))
        ways += (tempMen * tempWomen)
        initial_men += 1
        initial_women -= 1
        if(initial_men > men):
            break
    return ways

if __name__ == '__main__':
    t = (input().rstrip()).split(' ')
    print(chooser(int(t[0]),int(t[1]),int(t[2])))