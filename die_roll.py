n = input().rstrip().split()
w = int(n[0])
y = int(n[1])
count = 0
maxim = max(y, w)
for i in range(1, 7):
    if(i in range(maxim, 7)):
        count += 1
if(count==0):
    print('0/1')
elif(count==1):
    print('1/6')
elif(count==2):
    print('1/3')
elif(count==3):
    print('1/2')
elif(count==4):
    print('2/3')
elif(count==5):
    print('5/6')
elif(count==6):
    print('1/1')
