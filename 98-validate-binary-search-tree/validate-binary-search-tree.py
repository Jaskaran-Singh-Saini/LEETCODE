# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -math.inf

        stk = []

        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()

            if not root.val > prev: return False

            prev = root.val
            root = root.right

        return True