class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for _ in range(0,len(nums)-1):
            if nums[_]==nums[_+1]:
                return True
        return False