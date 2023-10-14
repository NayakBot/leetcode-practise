class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]

            first_step = cost[i] + dfs(i + 1)
            second_step = cost[i] + dfs(i + 2)
            dp[i] = min(first_step, second_step)
            return dp[i]

        return min(dfs(0), dfs(1))