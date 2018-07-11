# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, nodes = [],[root]
        cnt = 0
        while root and nodes:
            ans.append([v.val for v in nodes])
            lrnode = [(node.left, node.right) for node in nodes]
            nodes = [v for lrv in lrnode for v in lrv if v]
        for i in range(1,len(ans), 2):
            ans[i] = ans[i][::-1]
        return ans
