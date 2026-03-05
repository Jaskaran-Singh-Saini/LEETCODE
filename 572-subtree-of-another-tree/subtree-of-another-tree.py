# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False
        
        if self.isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSame(self, root, subRoot):
                if not root and not subRoot:
                    return True
                
                if root is None or subRoot is None:
                    return False
                
                if root.val != subRoot.val:
                    return False
                else:
                    return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)