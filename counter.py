def countWords(words1, words2) -> int:
    count = 0
    words1 = sorted(words1)
    words2 = sorted(words2)
    
    ptr1 = 0
    ptr2 = 0
    found = set()
    
    while(ptr1 < len(words1) and ptr2 < len(words2)):
        if((words1[ptr1] in found) or (words2[ptr2] in found)):
            count -= 1
            while((ptr1 < len(words1)) and (words1[ptr1] in found)):
                ptr1 += 1
            while((ptr2 < len(words2)) and (words2[ptr2] in found) ):
                ptr2 += 1

        else:
            if(words1[ptr1] == words2[ptr2]):
                count += 1
                found.add(words1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif(words1[ptr1] > words2[ptr2]):
                ptr2 += 1
            elif(words1[ptr1] < words2[ptr2]):
                ptr1 += 1
    if(ptr1 < len(words1)):
        if(words1[ptr1] in found):
            count -= 1
    if(ptr2 < len(words2)):
        if(words2[ptr2] in found):
            count -= 1
    return count

print(countWords(['a', 'b', 'cc', 'cc'], ['a', 'b', 'cc']))
print(countWords(['a', 'b', 'cc', 'cc', 'cc'], ['a', 'b', 'cc', 'cc', 'cc', 'cc']))