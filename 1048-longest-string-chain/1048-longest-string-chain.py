class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        n = len(words)
        words.sort(key=len)
        for wrd in words:
            dp[wrd] = max(dp.get( wrd[:i] + wrd[i + 1:], 0) + 1 for i in range(len(wrd)))
        return max(dp.values())