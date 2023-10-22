class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = k
        right = k
        min_val = nums[k]
        max_score = nums[k]

        while left > 0 or right < len(nums) - 1:
            if left == 0:
                right += 1
            elif right == len(nums) - 1:
                left -= 1
            else:
                if nums[left - 1] < nums[right + 1]:
                    right += 1
                else:
                    left -= 1

            min_val = min(min_val, nums[left], nums[right])
            score = min_val * (right - left + 1)
            max_score = max(max_score, score)

        return max_score