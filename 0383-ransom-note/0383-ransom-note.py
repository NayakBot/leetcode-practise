class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rHash = Counter(magazine)
        for c in ransomNote:
            if c in rHash and rHash[c] > 0:
                rHash[c] -= 1
            else:
                return False

        return True
        