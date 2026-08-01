class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            print(num)
            if num in seen:
                print('duplicate')
                return True
            seen.add(num)

            
        return False 


        