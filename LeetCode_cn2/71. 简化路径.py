class Solution:
    def simplifyPath(self, path: str) -> str:

        path_list = path.split('/')
        stack = list()

        for name in path_list:
            if name == '..':
                if stack:
                    stack.pop()
            elif name and name != '.':
                stack.append(name)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    pass