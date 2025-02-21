class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x=nums.count(0)
        for i in range(0,x):
            nums.remove(0)
            nums.append(0)
        