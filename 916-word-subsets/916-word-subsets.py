class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        words2Set = set(words2)
        counts2 = Counter("")
        for w2 in words2Set:
            counts2 = counts2 | Counter(w2) 
        for word1 in words1:
            good = True
            counts1 = Counter(word1)
            if counts1 | counts2 == counts1: 
                res.append(word1)
        return res