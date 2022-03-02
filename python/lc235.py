# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                # p, q, and LCA are in the left subtree
                root = root.left
            elif p.val > curr.val and q.val > curr.val:
                # p, q, and LCA are in the right subtree
                root = root.right
            else:
                # subtree containing both p and q has curr as root
                return root
