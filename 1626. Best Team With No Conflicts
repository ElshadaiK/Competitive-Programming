class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        dp = [p[1] for p in players]
        for i, (_, score) in enumerate(players):
            for j in [j for j in range(i) if players[j][1] <= score]:
                dp[i] = max(dp[i], dp[j] + score)
        return max(dp)
