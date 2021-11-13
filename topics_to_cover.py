def chooser(a, b):
    counter = 0
    holder = []
    store = {}
    ptr = -1
    for i in range(len(a)):
        diff = a[i] - b[i]
        holder.append(diff)
    
    holder.sort()
    
    for ind in range(len(holder)):
        if(holder[ind] > 0):
            ptr = ind
            break
    if(ptr == -1):
        return counter
    last = len(holder)
    for i in range(len(holder)):
        if(holder[i] in store):
            counter += store[holder[i]]
        else:
            if(holder[i] < 0):
                temp = abs(holder[i])
                for j in range(ptr, len(holder)):
                    if(holder[j] > temp):
                        store[holder[i]] = len(holder)-j
                        counter += store[holder[i]]
                        break
                
            elif(holder[i] == 0):
                res = len(holder)-ptr
                store[holder[i]] = res
                counter += store[holder[i]]
            else:
                finished = (len(holder)-i-1) * (len(holder)-i) // 2
                counter += finished
                break

    return counter

if __name__ == '__main__':
    n = int(input().rstrip())
    a = input().rstrip().split()
    b = input().rstrip().split()
    for i in range(n):
        a[i] = (int(a[i]))
        b[i] = (int(b[i]))
    print(chooser(a,b))