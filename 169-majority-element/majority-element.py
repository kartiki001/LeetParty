class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {} #Dictionary to store count of each element
        for i in nums:
            if i in count_dict:
                count_dict[i] +=1
            else:
                count_dict[i] =1
        return max(count_dict, key=count_dict.get) #return key with maximum value