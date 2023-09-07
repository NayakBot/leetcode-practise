class Solution:
    def jump(self, nums: List[int]) -> int:
        curLast = 0
        reach = 0
        count = 0
    
        n = len(nums)

        for i in range(n-1):
            reach = max(reach, i+nums[i])

            if reach >= n-1:
                count += 1
                break

            if i == curLast:
                curLast = reach
                count += 1
        
        return count