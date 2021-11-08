import math
def comb(items):
    count = 0
    total = 0
    store = {}
    for item in items:
        total += item
        count += 1
        if(item not in store):
            store[item] = 1
        else:
            store[item] += 1
    average = total/count
    answer = 0
    desired = average * 2
    if(int(desired) != desired):
        return answer
    visited = set()
    for key in store:
        if(key in visited):
            continue
        temp = desired - key
        if(temp in store):
            temp_val = store[temp]
            key_val = store[key]
            if(temp == key):
                visited.add(key)
                if(temp_val >= 2):
                    answer += (temp_val * (temp_val-1))/ 2
                    store[temp] = 0
            elif(temp_val != 0 and key_val != 0):
                answer += (temp_val * key_val)
                visited.add(key)
                visited.add(temp)
                store[temp] = 0
                store[key] = 0
    return int(answer)

if __name__ == '__main__':
    t = int(input().rstrip())
    output = []
    for i in range(t):
        holder = []
        n = int(input().rstrip())
        r = input().rstrip().split()
        for item in r:
            holder.append(int(item))
        output.append(holder)

    for elem in output:
        print(comb(elem))