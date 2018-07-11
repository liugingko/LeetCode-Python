# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, nodes = [],[root]
        while root and nodes:
            ans.append([v.val for v in nodes])
            lrnode = [(node.left, node.right) for node in nodes]
            nodes = [v for lrv in lrnode for v in lrv if v]
        return len(ans)
    def maxDepth(self, root):
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0