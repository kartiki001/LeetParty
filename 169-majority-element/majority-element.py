class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # MOORE'S VOTING ALGORITHM -->
        ele , count = nums[0], 1
        for i in range(1,len(nums)):
            count += 1 if nums[i] == ele else -1
            if count == 0:
                ele = nums[i+1]
        if nums.count(ele) > len(nums)/2:
            return ele

        # O(N) + O(N logN) -->
        # count_dict = {} # Dictionary to store count of each element
        # for i in nums:
        #     if i in count_dict:
        #         count_dict[i] +=1
        #     else:
        #         count_dict[i] =1
        # return max(count_dict, key=count_dict.get) # return key with maximum value