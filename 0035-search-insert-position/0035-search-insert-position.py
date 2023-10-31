class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bfs(l,h,target,nums):
            if l==h:
                return l if target<=nums[l] else l+1
            m = (l+h)//2

            if nums[m] == target:
                return m

            elif nums[m] > target:
                return bfs(l, m, target, nums)
            
            else:
                return bfs(m+1, h, target, nums)

        return bfs(0,len(nums)-1, target, nums)
                