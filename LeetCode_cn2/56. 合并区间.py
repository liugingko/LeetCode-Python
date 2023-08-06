from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) < 2: return intervals
        intervals.sort(key=lambda x: x[0], reverse=False)

        res = [intervals[0]]

        for i, e in enumerate(intervals, start=1):
            if res[-1][1] >= e[0]:
                res[-1][1] = max(e[1], res[-1][1])  # 合并选择最大的一个
            else:
                res.append(e)

        return res


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # [[1, 6], [8, 10], [15, 18]]


    print(Solution().merge(intervals))
