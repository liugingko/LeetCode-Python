import collections


class Solution(object):
    def shortestSubarray(self, A, K):

        n, dp = len(A), [0]  # 初始化dp[i] = A[0]+A[1]+...+A[i-1]
        for v in A: dp.append(dp[-1] + v)

        queue, res = collections.deque(), n + 1  # 初始化队列、结果变量
        for i in range(n+1):
            while queue and dp[i] <= dp[queue[-1]]:
                queue.pop()  # 出队, 删除不符合的

            while queue and dp[i] - dp[queue[0]] >= K:
                res = min(res, i - queue.popleft())  # 从左边出队，并更新最短距离。

            queue.append(i)  # 入队

        return res if res < n + 1 else -1  #返回最优解


if __name__ == '__main__':
    solu = Solution()
    A, K = [2, -1, 2], 3
    print(solu.shortestSubarray(A, K))