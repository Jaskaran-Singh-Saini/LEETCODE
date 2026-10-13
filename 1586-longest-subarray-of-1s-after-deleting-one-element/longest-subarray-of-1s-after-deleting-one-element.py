class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        mxl = 0
        start = 0
        zero = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                start = zero + 1
                zero = i
            mxl = max(mxl, i-start)
        return mxl