def calculate(s):
    return(max(sum(s[i] != s[i - 1] for i in range(1, len(s))) + (s[0] == '1') - 1, 0))
    
if __name__ == '__main__':
    t = int(input())
    result = []
    for _ in range(t):
        n, s = int(input()), input()
        result.append(calculate(s))
    for res in result:
        print(res)
