class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            o2t = defaultdict(set)
            t2o = defaultdict(set)
            for c1, c2 in zip(pattern, word):
                o2t[c1].add(c2)
                t2o[c2].add(c1)
            if all(len(v)==1 for v in o2t.values()) and all(len(v)==1 for v in t2o.values()):
                ans.append(word)
        return ans