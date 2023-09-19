class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sub = strs[0]

        for s in strs[1:]:
            n = len(s)
            for i, c in enumerate(sub):
                if i >= n or s[i] != c:
                    sub = sub[:i]
                    if i == 0:
                        return sub
                    break
            
        return sub
