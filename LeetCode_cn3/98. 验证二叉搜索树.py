# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def f(node, lower=float('-inf'), upper=float('inf')):

            if not node:
                return  True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not f(node.right, val, upper):
                return False
            if not f(node.left, lower, val):
                return False


            return True
        return f(root)