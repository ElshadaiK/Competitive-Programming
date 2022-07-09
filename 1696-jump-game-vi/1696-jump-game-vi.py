class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = deque()
        q.append(0)
        scores = [0 for _ in range(len(nums))]
        scores[0] = nums[0]
        for i in range(1, len(nums)):
            if(q[0] < i-k):
                q.popleft()
            scores[i] = scores[q[0]] + nums[i]
            while(len(q) > 0 and scores[q[-1]] <= scores[i]):
                q.pop()
            q.append(i)
        return scores[-1]