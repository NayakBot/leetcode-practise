class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        old = x

        if x < 0: return False

        while x:
            res = res*10 + x%10
            x = x // 10

        return old == res