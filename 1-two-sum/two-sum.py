class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for _ in range (0,len(nums)):
            if(nums.count(target-nums[_])>0):
                if(nums.index(target-nums[_])!=_):
                    return [_,nums.index(target-nums[_])]
            