class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if not len(s):
            return True

        if not len(t):
            return False
            
        for c in t:
            if s[i] == c:
                i += 1
            if i == len(s):
                return True

        return False