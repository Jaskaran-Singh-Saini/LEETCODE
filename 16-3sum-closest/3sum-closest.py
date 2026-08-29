class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        close = float('inf')

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue

            l, h = i+1, n-1

            while l<h:
                cur = nums[i] + nums[l] + nums[h]

                if abs(cur - target) < abs(close - target):
                    close = cur
                
                if cur == target:
                    return cur
                elif cur < target:
                    l += 1
                else:
                    h -= 1
            
        return close