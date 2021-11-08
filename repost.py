def reposter(listrs):
    store = {'polycarp': 1}
    maximum = 1
    for sentence in listrs:
        items = sentence.split()
        reposted_from = (items[2]).lower()
        reposter = (items[0]).lower()
        if(reposted_from in store):
            new = store[reposted_from] + 1
            store[reposter] = new
            maximum = max(maximum, new)
    return maximum

if __name__ == '__main__':
    n = int(input().rstrip())
    output = []
    for i in range(n):
        first_input = input().rstrip()
        output.append(first_input)

    print(reposter(output))