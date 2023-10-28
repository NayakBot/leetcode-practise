class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 0:
            return 0
        
        MOD = 10**9 + 7
        dp = [{} for _ in range(n+1)]
        
        for k in 'aeiou':
            dp[1][k] = 1

        for i in range(2, n+1):
            dp[i]['a'] = dp[i-1]['e']
            dp[i]['e'] = (dp[i-1]['a'] + dp[i-1]['i']) % MOD
            dp[i]['i'] = (dp[i-1]['a'] + dp[i-1]['e'] + dp[i-1]['o'] + dp[i-1]['u']) % MOD
            dp[i]['o'] = (dp[i-1]['i'] + dp[i-1]['u']) % MOD
            dp[i]['u'] = dp[i-1]['a']

        return sum(dp[n][k] for k in 'aeiou') % MOD