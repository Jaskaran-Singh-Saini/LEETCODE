class Solution:
    def numTrees(self, n: int) -> int:
        nTree = [1] * (n+1)

        for nodes in range(2,n+1):
            res = 0
            for root in range(1, nodes+1):
                l = root -1
                r = nodes - root
                res += nTree[l] * nTree[r]
            nTree[nodes] = res
        return nTree[n]