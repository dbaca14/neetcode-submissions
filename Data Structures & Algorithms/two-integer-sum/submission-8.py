class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                j = seen[diff]
                idx = [i, j]
                return sorted(idx)
            seen[num] = i
