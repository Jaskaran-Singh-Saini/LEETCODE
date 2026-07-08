# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        mp = { 0:[], 1:[TreeNode()] }

        def FBT(n):
            if n in mp:
                return mp[n]
            
            res = []
            for l in range(n):
                r = n-l-1

                lft = FBT(l)
                rght = FBT(r)
                for t1 in lft:
                    for t2 in rght:
                        res.append(TreeNode(0,t1,t2))
            mp[n] = res
            return res
        return FBT(n)