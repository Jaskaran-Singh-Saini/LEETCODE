# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(cur):
            if not cur:
                return 0
            
            lxtra = dfs(cur.left)
            rxtra = dfs(cur.right)
            xtraCoin = cur.val -1 + lxtra + rxtra
            self.res += abs(xtraCoin)
            return xtraCoin
        dfs(root)
        return self.res