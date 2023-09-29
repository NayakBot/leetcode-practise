class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n <= 2: return True
				
        isGreat = False
        isLess = False
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                isGreat = True
            if nums[i - 1] < nums[i]:
                isLess = True

            if isGreat and isLess:
                return False

        return True
