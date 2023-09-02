class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for _ in range(k):
            i = nums.pop(n-1)
            nums.insert(0, i)
