class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        return int(sum([i * (i - 1) / 2 for _,i in c.items()]))