class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s3 = -inf
        stack = []

        for n in nums[::-1]:
            if n < s3:
                return True
            
            while stack and stack[-1] < n:
                s3 = stack.pop()
            
            stack.append(n)
        
        return False