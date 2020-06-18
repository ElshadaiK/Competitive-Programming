# cook your dish here
try:
    x = input()
except EOFError:
    print ("EOFError")
    x = 0

x = int(x)
cases = []
for i in range(x):
    try:
        n = eval(input())
        a = input().split()
    except EOFError:
        print ("EOFError")
        break
    case = [n, a]
    cases.append(case)
def icecream():
    for b in cases:
        fives = []
        tens = []
        fifteens = []
        status = ""
        for i in range(b[0]):
            if b[1][i] == "5":
                fives.append(b[1][i])
                status = "YES"
            elif b[1][i] == "10":
                if(len(fives) > 0):
                    x = fives.pop()
                    tens.append(b[1][i])
                    status = "YES"
                else:
                    status = "NO"
                    print(status)
                    break
            else:
                if(len(tens)>  0):
                    x = tens.pop()
                    fifteens.append(b[1][i])
                    status = "YES"
                elif(len(fives) > 1):
                    x = fives.pop()
                    x = fives.pop()
                    fifteens.append(b[1][i])
                    status = "YES"
                else:
                    status = "NO"
                    print(status)
                    break
        if(status == "YES"):
            print("YES")
icecream()
                
        
