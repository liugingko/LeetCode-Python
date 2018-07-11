class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False  # 长度不相等的情况
        if A == B:  # 两个字符串相等的情况，A必须存在重复字符
            seen = set()
            for a in A:
                if a in seen: return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in zip(A, B):  # A、B不相等的情况
                if a != b:
                    pairs.append([a, b])
                if len(pairs) > 2: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


if __name__ == '__main__':
    solu = Solution()
    print(solu.buddyStrings(A='ab', B='ba'))