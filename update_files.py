import math
def updater2(comp, cables):
    comp -= 1
    capacity = math.floor(math.log(cables, 2))
    hours = capacity+1
    if(capacity == 0):
        return comp
    
    total = comp - (((2)**(capacity+1))-1)
    if(total <= 0):
        now = math.ceil(math.log(comp+1, 2))
        return now
    elif(total == 1):
        now = 1
    else:
        now = math.ceil(total/(cables))
    return now+hours
  


def updater(comp, cables):
    comp -= 1
    total = 0
    hours = 0
    nex = 1
    
    while(total < comp):
        if(nex < cables):
            hours += 1
            total += nex
            nex *= 2
        elif(nex == cables):
            hours += 1
            total += nex
        else:
            nex = cables
            hours += 1
            total += nex
        
    return hours

if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    for i in range(t):
        inp = (input().rstrip()).split()
        comps = int(inp[0])
        cables = int(inp[1])
        temp.append([comps,  cables])
    for items in temp:
        print(updater2(items[0], items[1]))


