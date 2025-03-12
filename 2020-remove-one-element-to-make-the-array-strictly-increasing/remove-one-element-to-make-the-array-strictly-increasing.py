class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:  # Found a decreasing pair
                count += 1
                if count > 1:
                    return False  # More than one removal required
                
                # Check if skipping nums[i-1] OR nums[i] keeps the order
                if i > 1 and nums[i] <= nums[i - 2]:
                    nums[i] = nums[i - 1]  # Skip nums[i] instead of nums[i-1]
        
        return True