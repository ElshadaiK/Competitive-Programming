from typing import DefaultDict


def sortCoins(listr):
    map_to_greater = {}

    for string in listr:
        # A>B, A<B
        oper = string[1]
        if oper == "<":
            if string[0] not in map_to_greater:
                map_to_greater[string[0]] = set() 
            map_to_greater[string[0]].add(string[2])
        else:
            if string[2] not in map_to_greater:
                map_to_greater[string[2]] = set() 
            map_to_greater[string[2]].add(string[0])
            
    if len(map_to_greater) == 3:
        return("Impossible")
    result = ""
    greatest = ""
    if "A" not in map_to_greater:
        greatest = "A"
        result += "A"
    elif "B" not in map_to_greater:
        greatest = "B"
        result += "B"
    elif "C" not in map_to_greater:
        greatest = "C"
        result += "C"

    while map_to_greater:
        for k in map_to_greater:
            v = map_to_greater[k]
            if greatest in v:
                v.remove(greatest)


        for k in map_to_greater:
            v = map_to_greater[k]
            if len(v) == 0:
                greatest = k 
                result = greatest +result   
                del map_to_greater[k]
                break
         
    return result


if __name__ == '__main__':
    
    output = []
    for i in range(3):
        first_input = input().rstrip()
        output.append(first_input)

    print(sortCoins(output))
