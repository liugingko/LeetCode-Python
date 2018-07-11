# @Time   :2018/6/25
# @Author :LiuYinxing
# 解题思路 深度优先，递归


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.re = 0  # 用于记录每个节点的最长路径

    def longestUnivaluePath(self, root):
        def f(root, n):
            if root == None: return 0
            left = f(root.left, root.val)  # 获取左分支节点与当前节点的最长路径
            right = f(root.right, root.val)  # 获取右分支节点与当前节点的最长路径
            self.re = max(self.re, left + right)  # 获取当前节点的最长路径，并更新记录
            return max(left, right) + 1 if root.val == n else 0  # 当前节点与父节点的值是否相同，如果相同就在子节点加一

        f(root, 0)
        return self.re