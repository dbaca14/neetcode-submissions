class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        seen = set(nums)
        longest = 0

        for num in seen:
            if num-1 not in seen:
                length = 1
                nextNum = num+1 

                while nextNum in seen:
                    length += 1
                    nextNum += 1
                longest = max(length, longest)
        return longest