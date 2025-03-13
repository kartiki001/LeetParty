class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one, count = 0,0
        for i in nums:
            if i==1:
                count+=1
            else:
                max_one = max(max_one, count)
                count = 0
        return max(max_one, count)