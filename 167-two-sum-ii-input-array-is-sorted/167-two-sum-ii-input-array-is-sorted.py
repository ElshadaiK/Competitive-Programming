class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if(num in store):
                return [store[num], i+1]
            store[target-num] = i+1
                