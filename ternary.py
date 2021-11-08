def ternary(numstr):
    shortest = 20000
    ptr = 0
    res = set()
    for i in range(len(numstr)):
        holder = set()
        if(not res):
            res = set(i)
        else:
            holder.remove(res[0])
            res.pop(0)
        j = i+1
        holder.add(numstr[i])
        while(len(holder) < 3 and j<len(numstr)):
            if(numstr[j] not in holder):
                holder.add(numstr[j])
                res.add(j)
