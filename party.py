from collections import deque
def grouper(employees):
    que = deque([])
    counts = {}
    bosses = {}
    zeros = set()
    for i in range(len(employees)):
        if(i+1 not in bosses):
            bosses[i+1] = set()
        if(int(employees[i]) == -1):
            counts[i+1] = 0
            if(i+1 not in bosses):
                bosses[i+1] = set()
            zeros.add(i+1)
        else:
            counts[i+1] = 1
        
            if(employees[i] not in bosses):
                bosses[employees[i]] = set()

            bosses[employees[i]].add(i+1)
    for zero in zeros:
        que.append(zero)
    counter = 0
    while(que):
        size = len(que)
        itr = 0
        while(itr < size):
            itr += 1
            current = que.popleft()
            for employee in bosses[current]:
                counts[employee] -= 1
                if(counts[employee] == 0):
                    que.append(employee)
        counter += 1
    return counter

if __name__ == '__main__':
    n = int(input().rstrip())
    temp = []
    for i in range(n):
        supervisor = int(input().rstrip())
        temp.append(supervisor)
    print(grouper(temp))