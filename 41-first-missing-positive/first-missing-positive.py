class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if 1 in nums:
            i=nums.index(1)
            j=1
            while i<len(nums):
                if nums[i]!=j:
                    return j
                i+=1
                j+=1
            return j
        return 1