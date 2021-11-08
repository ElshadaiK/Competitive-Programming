import math
def gcd(num1, num2):
    if(num1 == num2):
        return num1
    
    return 1
        

def reader():
    n = input().rstrip()
    m = n.split()
    print(gcd(m[0],m[1]))

reader()