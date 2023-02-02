def layer_maker(layer, creams):
    for i in range(layer-2, -1, -1):
        creams[i] = max(creams[i], max(0, creams[i+1]-1))
    for i in range(len(creams)):
        creams[i] = "1" if creams[i] > 0 else "0"
    res = " ".join(creams)
    return res


if __name__ == '__main__':
    t = int(input().rstrip())
    res = []
    for i in range(t):
        layer = int(input().rstrip())
        creams = input().rstrip().split(' ')
        for i in range(len(creams)):
            creams[i] = int(creams[i])
        res.append(layer_maker(layer, creams))
    for ans in res:
        print(ans)
