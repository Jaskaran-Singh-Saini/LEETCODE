class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        numi = numj = float('inf')

        for num in nums:
            if num <= numi:
                numi = num
            elif num <= numj:
                numj = num
            else:
                return True
            
        return False