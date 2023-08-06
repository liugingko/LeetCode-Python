# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        my_dict = {}

        def copynode(node):

            if node is None: return None
            if my_dict.get(node): return my_dict.get(node)

            root = Node(node.val)  # 存入字典
            my_dict[node] = root

            root.next = copynode(node.next)  # 继续获取下一个节点
            root.random = copynode(node.random)  # 继续获取下一个随机节点

            return root

        return copynode(head)