class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = k = 0
        n = len(nums)

        while k < n:
            check = nums[k]
            while k < n and nums[k] == check:
                k += 1

            nums[index] = nums[k-1]
            index += 1

        return index

