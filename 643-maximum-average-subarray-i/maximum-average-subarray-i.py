class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        curSum = 0

        for i in range(k):
            curSum += nums[i]
        maxAvg = curSum/k

        for i in range(k,n):
            curSum += nums[i]
            curSum -= nums[i-k]

            maxAvg = max(maxAvg,curSum/k)
        
        return maxAvg