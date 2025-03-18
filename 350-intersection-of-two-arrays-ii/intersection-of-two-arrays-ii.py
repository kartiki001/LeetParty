class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        for i in nums1:
            if i in nums2:
                res.append(i)
                print(nums2.remove(i))
        return res