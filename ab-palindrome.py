def palindrome(a, b, word):
    store = {'0': 0, '1': 0, '?': 0}
    for i in word:
        store[i] += 1
    
    if(store['0'] > a or store['1'] > b or (store['1'] + store['0'] + store['?'] > a+b)):
        return -1
    c0 = a - store['0']
    c1 = b - store['1']
    holder = list(word)
    i = 0
    n = len(word)
    saved = set()
    while(c1 >= 0 and c0 >= 0 and i < n//2):
        if(holder[i] != '?' and holder[n-i-1] != '?'):
            if(holder[i] != holder[n-i-1]):
                return -1
        
        elif(holder[i] != '?' or holder[n-i-1] != '?'):
            if(holder[i] == '?'):
                if(holder[n-i-1] == '1'):
                    holder[i] = '1'
                    c1 -= 1
                else:
                    holder[i] = '0'
                    c0 -= 1
            
            elif(holder[n-i-1] == '?'):
                if(holder[i] == '1'):
                    holder[n-i-1] = '1'
                    c1 -= 1
                else:
                    holder[n-i-1] = '0'
                    c0 -= 1


        elif(holder[i] == '?' and holder[n-i-1] == '?'):
            saved.add(i)
        
        i += 1
    i = 0
    if(len(saved) > 0):
        while(c1 >= 0 and c0 >= 0 and i < n//2):
            if(i in saved):
                if(c0 >= 2 and c1 >= 2):
                    holder[i] = '1'
                    holder[n-i-1] = '1'
                    c1 -= 2
                
                elif(c1 >= 2):
                    holder[i] = '1'
                    holder[n-i-1] = '1'
                    c1 -= 2
                
                elif(c0 >= 2):
                    holder[i] = '0'
                    holder[n-i-1] = '0'
                    c0 -= 2

                else:
                    return -1
            
            i += 1
    i = n//2
            
    if(c1>0 and c0>0):
        return -1
    elif(c1 <0 or c0<0):
        return -1
    elif(c1==1 or c0==1) and n%2==1:
        if(c0 == 1):
            holder[i] = '0'
        else:
            holder[i] = '1'
    elif(c1 >0 or c0 >0):
        return -1
    
    result = ""
    for i in holder:
        result += str(i)
    return result

if __name__ == '__main__':
    t = int(input().rstrip())
    temp = []
    for i in range(t):
        first_input = input().rstrip().split()
        a = int(first_input[0])
        b = int(first_input[1])
        second_input = input().rstrip()
        
        temp.append([a,b,second_input])
    for items in temp:
        print(palindrome(items[0], items[1], items[2]))