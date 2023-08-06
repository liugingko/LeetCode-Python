class Solution:
    def findAnagrams(self, s: str, p: str):
        s_len, p_len = len(s), len(p)

        if s_len < p_len: return []

        res = []

        s_count = [0] * 26
        p_count = [0] * 26

        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            res.append(0)

        for i in range(s_len - p_len):
            print(i)
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i+p_len]) - 97] += 1

            if s_count == p_count:
                res.append(i+1)

        return res


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s,p))

