# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGN(root, float(-inf))
    
    def countGN(self, node, mx):
        if not node:
            return 0
        
        count = 0

        if node.val >= mx:
            count = 1
            mx = node.val
        
        count += self.countGN(node.left, mx)
        count += self.countGN(node.right, mx)

        return count