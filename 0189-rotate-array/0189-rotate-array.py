class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if k>n:
            k = k%n
        for i in range(n//2):
            t = nums[i]
            nums[i] = nums[n-i-1]
            nums[n-i-1] = t
        

        for i in range(k//2):
            t = nums[i]
            nums[i] = nums[k-i-1]
            nums[k-i-1] = t


        for i in range(k,k+(n-k)//2):
            t = nums[i]
            nums[i] = nums[k+n-i-1]
            nums[k+n-i-1] = t