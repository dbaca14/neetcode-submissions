class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        size = len(nums)

        output = [None] * size

        prod = 1
        
        for i in range(size):
            output[i] = prod

            prod *= nums[i] 
        
        prod = 1
        for i in range(size -1, -1, -1):
            output[i] *= prod

            prod *= nums[i]

        return output
                    
