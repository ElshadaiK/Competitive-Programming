class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:(-x[1],x[0]))
        total = 0
        units = 0
        i = 0
        while(total<truckSize and i < len(boxTypes)):
            amount = boxTypes[i][0]
            size = boxTypes[i][1]
            if(total+amount <= truckSize):
                units += amount*size
                total += amount
            else:
                units += (truckSize-total)*size
                total += amount
            i += 1
        return units