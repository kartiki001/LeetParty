class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n^res #XOR all the numbers as 1^1 =0 and 0^0 = 0 else 1. eqyal XORs cancel out each othet
        return res