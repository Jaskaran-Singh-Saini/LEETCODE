# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def maxGain(node):
            if not node:
                return 0
            
            lftGain = max(maxGain(node.left), 0)
            rghtGain = max(maxGain(node.right), 0)

            currPath = node.val + lftGain + rghtGain

            self.maxSum = max(self.maxSum, currPath)

            return node.val + max(lftGain, rghtGain)
        
        maxGain(root)

        return self.maxSum