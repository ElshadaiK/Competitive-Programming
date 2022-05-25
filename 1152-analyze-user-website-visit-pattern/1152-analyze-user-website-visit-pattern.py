class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_page_list = [(user, page) for time, user, page in sorted(zip(timestamp, username, website))]
        store = defaultdict(list)
        for user, page in user_page_list:
            store[user].append(page)
        store = {key: set(combinations(value, 3)) for key, value in store.items()}
        
        patterns = [item for sublist in store.values() for item in sublist]
        counts = sorted(Counter(patterns).items(), key=lambda x: (-x[1],x[0]))
        return (list(counts[0][0]))
                          