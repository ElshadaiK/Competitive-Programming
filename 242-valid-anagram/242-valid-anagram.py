class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}
        if(len(s) != len(t)):
            return False
        for i in s:
            if i not in store:
                store[i] = 0
            store[i] += 1
        for i in t:
            if i not in store or store[i] == 0:
                return False
            store[i] -= 1
        return True