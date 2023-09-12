class Solution:
    def minDeletions(self, s: str) -> int:
        charMap = {}
        for c in s:
            if c in charMap:
                charMap[c] += 1
            else:
                charMap[c] = 1
        
        done = set()
        ans = 0

        for c, count in charMap.items():
            while count > 0 and count in done:
                count -= 1
                ans += 1
            done.add(count)
        
        return ans