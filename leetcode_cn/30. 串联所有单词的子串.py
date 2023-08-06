class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:return []
        all_len = sum(map(len, words))
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i+all_len]
            flag = True
            for key in words:
                if words[key] != tmp.count(key):
                    flag = False
                    break
            if flag:res.append(i)
        return res