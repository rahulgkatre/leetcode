# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                # p, q, and LCA are in the left subtree
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                # p, q, and LCA are in the right subtree
                curr = curr.right
            else:
                # subtree containing both p and q has curr as root
                return curr
