class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [1] * n

        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                ans[i+1] = max(1 + ans[i], ans[i+1])
        
        for i in range(n-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                ans[i-1] = max(1 + ans[i], ans[i-1])

        return sum(ans)