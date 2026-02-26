# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        def order(node, level):
            if not node:
                return
            if len(self.res) == level:
                self.res.append([])
            
            self.res[level].append(node.val)

            if node.left:
                order(node.left, level+1)
            
            if node.right:
                order(node.right, level+1)
            
            if not root:
                return self.res

        order(root, 0)
        return self.res