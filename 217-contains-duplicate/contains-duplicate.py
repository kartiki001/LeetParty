class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #created a hashmap

        for i in nums:
            if i in hashset: #check if number already present in hash map
                return True
            hashset.add(i) #added number to hashmap
        return False

        # nums.sort()
        # for _ in range(0,len(nums)-1):
        #     if nums[_]==nums[_+1]:
        #         return True
        # return False