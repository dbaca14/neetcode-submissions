from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step 1: Initialize running multipliers
        l_mult = 1
        r_mult = 1
        n = len(nums)
        
        # Step 2: Create blank arrays for left and right products
        l_arr = [0] * n
        r_arr = [0] * n
        
        # Step 3: Populate both arrays in a single pass
        for i in range(n):
            # Calculate the corresponding index from the back
            j = -i - 1
            
            # Store the current running products
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            
            # Update the running multipliers for the next iteration
            l_mult *= nums[i]
            r_mult *= nums[j]
            
        # Step 4: Zip and multiply matching indices for the final output
        return [l * r for l, r in zip(l_arr, r_arr)]
