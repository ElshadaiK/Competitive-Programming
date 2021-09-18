def pigger(inp):
    result = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    lines = inp.split(' \n ')
    for line in lines:
        words = line.split(' ')
        print(words)
        for word in words:
            hold = word
            for i in word:
                if i in vowels:
                    toBe = hold
                    break
                else:
                    hold = hold[1:] + hold[0]
            if(hold == word):
                toBe += 'yay '
            else:
                toBe += 'ay '
            result += toBe
        result += '\n'
    return result
    