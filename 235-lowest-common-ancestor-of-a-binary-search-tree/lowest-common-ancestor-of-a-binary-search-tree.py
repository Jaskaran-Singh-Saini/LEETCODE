# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None

        if root == p or root == q:
            return root
        
        lft = self.lowestCommonAncestor(root.left, p, q)
        rght = self.lowestCommonAncestor(root.right, p, q)

        if lft and rght: return root

        return lft if lft else rght