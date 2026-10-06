class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        pair = 0

        for num in nums:
            if d[k-num] > 0:
                pair += 1
                d[k-num] -= 1
            else:
                d[num] += 1
        return pair