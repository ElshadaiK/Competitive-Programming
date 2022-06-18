class WordFilter:
    def __init__(self, words: List[str]):
        self.map = {f'{w[:i]}#{w[j:]}': weight for weight, w in enumerate(words)
                   for i in range(len(w) + 1) for j in range(len(w) + 1)}
        # print(self.map)

    def f(self, prefix: str, suffix: str) -> int:
        return self.map.get(f'{prefix}#{suffix}', -1)        



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)