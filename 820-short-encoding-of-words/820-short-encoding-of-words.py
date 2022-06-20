class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: -len(x))
        visited = set()
        ans = 0
        for word in words:
            if word not in visited: 
                for i in range(len(word)-1, -1, -1):
                    visited.add(word[i:])
                ans += 1 + len(word)
        return ans