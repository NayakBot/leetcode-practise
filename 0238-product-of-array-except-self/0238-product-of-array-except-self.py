class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        postfix = 1
        n = len(nums)

        for i, num in enumerate(nums):
            output[i] *= prefix
            prefix *= num
        
        for i, num in enumerate(nums[::-1]):
            output[n-i-1] *= postfix
            postfix *= num
        
        return output