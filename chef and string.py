try:
    x = input()
except EOFError:
    print ("EOFError")
    x = 0

x = int(x)
cases = []
for i in range(x):
    case = []
    try:
        students = input()
        for student in students:
            case.append(student)
    except EOFError:
        print ("EOFError")
        break
    cases.append(case)
#print(cases)
def dance():
    for b in cases:
        if(len(b) == 1):
            print(0)
        else:
            pairs = 0
            i = 1
            while(i < len(b)):
                if((b[i] == "x" and b[i-1] == "y") or (b[i] == "y" and b[i-1] == "x")):
                    pairs += 1
                    i = i + 2
                else:
                    i = i + 1
                    pass
            print(pairs)
dance()
    
                
                                    
