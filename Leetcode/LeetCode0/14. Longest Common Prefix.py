class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n==0:return ''
        if n==1:return strs[0]
        rstr = ''
        slong = len(strs[0])
        for i in range(slong):
            tar = strs[0][i]
            just = 0
            for v in strs[1:]:
                print(i , len(v))
                if i >= len(v):
                    just = 0
                    break
                if tar == v[i]:
                    just = 1
                else:
                    just = 0
                    break
            if just == 1:
                rstr = rstr + tar
            else:
                return rstr
        return rstr

    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = strs
        import os
        return os.path.commonprefix(strs)
if __name__ == '__main__':
    solu = Solution()
    strs = ["aa","a"]
    strs = ["aca","cba"]
    print(solu.longestCommonPrefix(strs))