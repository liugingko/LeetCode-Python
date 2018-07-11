# @Time   :2018/6/18
# @Author :LiuYinxing


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        store, maxlen, start, idx = {}, 0, 0, 0         # 初始化 store, 子串的长度， 开始位置， 当前字符位置
        for idx, char in enumerate(s, 1):               # 依次向右，判断 计算
            if char in store and start <= store[char]:  # 出现重复字符串，更新子串的开始位置
                start = store[char]
            store[char] = idx                  # 更新 store
            maxlen = max(maxlen, idx - start)  # 更新 maxlen
        return maxlen or idx                  # 考虑字符串长度为0的情况


if __name__ == '__main__':
    solu = Solution()
    s = 'abcabcbb'
    print(solu.lengthOfLongestSubstring(s))