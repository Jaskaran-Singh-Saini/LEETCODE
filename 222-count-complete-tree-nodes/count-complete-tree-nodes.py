# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)

        if lh == rh: return (1<<lh) + self.countNodes(root.right)
        else: return (1<<rh) + self.countNodes(root.left)
    
    def getHeight(self,node):
        h=0
        while node:
            h+=1
            node = node.left
        return h