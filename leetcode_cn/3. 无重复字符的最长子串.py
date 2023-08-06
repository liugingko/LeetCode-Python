class Solution:
    def lengthOfLongestSubstring(self, s):

        windows = set()
        n = len(s)

        rk, max_sub_len = -1, 0
        for i in range(n):
            if i > 0:
                windows.remove(s[i-1])  # 滑动窗口向右边移动一下，所以要删除之前的开头

            while rk + 1 < n and s[rk+1] not in windows:
                windows.add(s[rk+1])
                rk += 1

            max_sub_len = max(max_sub_len, len(windows))

        return max_sub_len


