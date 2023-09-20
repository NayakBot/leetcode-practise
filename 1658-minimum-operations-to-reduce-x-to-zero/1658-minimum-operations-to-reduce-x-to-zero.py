class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)

        target = sum(nums) - x

        l = curVal = 0
        window = -1

        for r in range(n):
            curVal += nums[r]

            while l <= r and curVal > target:
                curVal -= nums[l]
                l += 1

            if curVal == target:
                window = max(window, r - l + 1)
                
        return -1 if window == -1 else n - window