# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 1
        def tree(node):

            if not node:return 0

            l = tree(node.left)
            r = tree(node.right)
            self.res = max(self.res, l + r + 1)

            return max(l ,r ) + 1

        tree(root)
        return self.res -1
