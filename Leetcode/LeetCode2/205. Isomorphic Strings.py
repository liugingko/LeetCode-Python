# @Time   :2022/1/27
# @Author :lyx


class Solution:
    def isIsomorphic(self, s, t):
        s_hash = {}
        t_hash = {}
        for s1, t1 in zip(s, t):
            # print(s1, t1)
            if s_hash.get(s1):
                if s_hash[s1] == t1:
                    continue
                else:
                    return False
            else:
                if t_hash.get(t1):
                    return False
                else:
                    s_hash[s1] = t1
                    t_hash[t1] = 1
        # print(s_hash, t_hash)
        return True





if __name__ == '__main__':
    solu = Solution()
    s = "egg"
    t = "add"
    s = "foo"
    t = "bar"
    print(solu.isIsomorphic(s, t))