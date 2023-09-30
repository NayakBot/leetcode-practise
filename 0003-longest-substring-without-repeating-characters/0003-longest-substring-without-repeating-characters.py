class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cur = set()
        ans = 0
        for r in range(len(s)):
            cur.add(s[r])

            if len(cur) == (r - l + 1):
                ans = max(ans, r - l + 1)
            else:
                while len(cur) != (r - l + 1):
                    if s[l] != s[r]:
                        cur.discard(s[l])
                    l += 1
                    
        return ans 