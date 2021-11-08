def  songs(moments, songs):
    answer = [0 for _ in range(len(moments))]
    ptr = 0
    so_far = 0
    searcher = 0
    for i in range(len(songs)):
        j = songs[i].split()
        ci = j[0]
        ti = j[1]
        total = int(ci)*int(ti)
        for k in range(searcher, len(moments)):
            if(int(moments[k]) in range(ptr, total+1+so_far)):
                answer[k] = i+1
            elif(int(moments[k]) >= total+1+so_far):
                searcher = k
                break
        ptr = total+1+so_far
        so_far+= total
    for ans in answer:
        print(ans)

if __name__ == '__main__':
    n = (input().rstrip()).split()
    m = int(n[1])
    n = int(n[0])
    output = []
    for i in range(n):
        first_input = input().rstrip()
        output.append(first_input)
    second_input = input().rstrip().split()
    songs(second_input, output)