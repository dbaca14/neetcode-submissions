class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}

       for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            idx = seen.get(diff) 
            return [idx, i]

        seen[num] = i