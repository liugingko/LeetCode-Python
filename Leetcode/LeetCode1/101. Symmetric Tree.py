'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(tleft, tright):
            if tleft == None and tright == None: return True
            if tleft == None or tright == None: return False
            return tleft.val == tright.val and isMirror(tleft.left, tright.right) and isMirror(tleft.right, tright.left)
        return isMirror(root, root)

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        return self.isMirror(root, root)
    def isMirror(self, tleft, tright):
        if tleft == None and tright == None: return True
        if tleft == None or tright == None: return False
        return tleft.val == tright.val and self.isMirror(tleft.left, tright.right) and self.isMirror(tleft.right, tright.left)

