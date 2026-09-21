class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put nums as a set
        seen = set(nums)
        longest = 0

        for num in nums:
            # check if current number is first in sequence
            if num - 1 not in seen:
                next_num = num + 1
                length = 1
                # count sequence until it breaks
                while next_num in seen:
                    length += 1
                    next_num += 1
                # compare current seq with longest found
                longest = max(longest, length)

        return longest

        