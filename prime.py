import math
def prime(num):
    if(num <= 2):
        return -1
    num -= 2
    if(math.sqrt(num) == math.floor(math.sqrt(num))):
        return -1
    counter = 2
    found = False
    while(counter < math.sqrt(num)):
        if(num%counter == 0):
            found = True
            break
        counter += 1
    if(found == True):
        return -1
    else:
        result = "2 " + str(num)
        return result
        

def reader():
    n = int(input())
    print(prime(n))

reader()