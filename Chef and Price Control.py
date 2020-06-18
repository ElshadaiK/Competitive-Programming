# cook your dish here
try:
    test = input()
except EOFError:
    print ("EOFError")
    test = 0

test = int(test)
cases = []
for i in range(test):
    try:
        m = input().split()
        n = eval(m[0])
        k = eval(m[1])
        items = input().split()
    except EOFError:
        print ("EOFError")
        break
    case = [n, k, items]
    cases.append(case)
#print(cases)
def priceControl():
    for b in cases:
        loss = 0
        for i in range(b[0]):
            if eval(b[2][i]) > b[1]:
                loss += eval(b[2][i])- b[1]
            else:
                pass
        print(loss)
priceControl()

                
        
