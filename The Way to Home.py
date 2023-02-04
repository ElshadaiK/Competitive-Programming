def frog_jumps(n, d, s):
    current_position = 1
    jump_count = 0
    while current_position < n:
        next_position = min(n-1,current_position+d-1)
        while s[next_position] == '0':
            next_position -= 1
        if next_position + 1 == current_position:
            return -1
        current_position = next_position + 1
        jump_count += 1
    return jump_count

n, d = map(int, input().split())
s = input().strip()
print(frog_jumps(n, d, s))