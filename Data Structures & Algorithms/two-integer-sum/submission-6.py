class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0

        for num in nums:
            diff = target - num
            if diff in seen:
                j = seen[diff]
                idx = [i, j]
                return sorted(idx)
            seen[num] = i
            i += 1
