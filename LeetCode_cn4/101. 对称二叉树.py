# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(p, q):

            if not p and not q:
                return True
            if not p or not q:
                return False

            return p.val == q.val and dfs(p.left, q.right) and dfs(q.right, p.left)

        return dfs(root, root)
