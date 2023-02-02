def decodeCiphertext(encodedText: str, rows: int) -> str:
    words_len = len(encodedText)//rows
    words = []
    i = 0
    start = 0
    while(i<len(encodedText)+1):
        if(i%words_len == 0 and i != 0):
            word = encodedText[start:i]
            words.append(word)
            start =  i
        i += 1
    result = ""
    j = 0
    while(j < (words_len)):
        if(j == words_len-1):
            break
        else:
            i = 0
            while(i < len(words) and i+j < words_len):
                result += str(words[i][i+j])
                i += 1
        j += 1
    return (result)

print(decodeCiphertext("ch   ie   pr", 3))