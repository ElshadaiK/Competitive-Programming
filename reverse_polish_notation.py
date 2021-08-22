def evalRPN(tokens):
    holder = []
    for i in tokens:
        if i.isnumeric() or len(i) > 1:
            holder.append(i)
        else:
            p1 = holder.pop()
            p2 = holder.pop()
            res = 0
            if(i == '+'):
                res = int(p1) + int(p2)
            elif(i == '-'):
                res = int(p2) - int(p1)
            elif(i == '*'):
                res = int(p2) * int(p1)
            elif(i == '/'):
                res = int(p2) / int(p1)
            
            holder.append(res)
    return int(holder[0])
            