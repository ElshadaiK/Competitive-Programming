def isValid(s):
    vals = []
    for i in s:
        if(i == '{' or i == '[' or i == '('):
            vals.append(i)
        else:
            if(vals == []):
                return False
            elif(i == ']'):
                top = vals.pop()
                if(top != '['):
                    return False
            elif(i == ')'):
                top = vals.pop()
                if(top != '('):
                    return False
            elif(i == '}'):
                top = vals.pop()
                if(top != '{'):
                    return False
    print(vals)
    if(vals != []):
        return False
    return True