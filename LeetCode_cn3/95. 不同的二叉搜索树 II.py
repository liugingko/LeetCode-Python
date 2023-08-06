# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def tree(start, end):

            if start > end:
                return [None]

            alltree = []

            for i in range(start, end+1):
                lefttree = tree(start, i-1)
                rigthtree = tree(i+1, end)

                for l in lefttree:
                    for r in rigthtree:
                        cur_tree = TreeNode(i, l, r)
                        alltree.append(cur_tree)
            return alltree

        return tree(1, n) if n else []
