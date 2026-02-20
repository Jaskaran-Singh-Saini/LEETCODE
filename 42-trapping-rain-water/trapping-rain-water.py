class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        l_max = height[0]
        r_max = height[r]
        sum = 0

        while l<r:
            if height[l]<height[r]:
                l_max = max(l_max, height[l])
                if l_max-height[l]>0:
                    sum += l_max-height[l]
                l+=1
            
            else:
                r_max = max(r_max, height[r])
                if r_max-height[r] > 0:
                    sum += r_max-height[r]
                r-=1
        return sum