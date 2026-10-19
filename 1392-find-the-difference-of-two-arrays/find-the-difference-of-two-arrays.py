class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        n1set, n2set = set(nums1), set(nums2)

        res1, res2 = set(), set()

        for n in nums1:
            if n not in n2set:
                res1.add(n)

        for n in nums2:
            if n not in n1set:
                res2.add(n)

            
        return [list(res1), list(res2)]