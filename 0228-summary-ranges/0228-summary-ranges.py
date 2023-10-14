class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        cur = ''
        for i in range(len(nums)):
            if cur == '':
                cur = f'{nums[i]}'
            if i == len(nums) - 1 or nums[i] < nums[i + 1] - 1:
                if int(cur) != nums[i]:
                    cur += f'->{nums[i]}'
                
                res.append(cur)
                cur = ''

        return res