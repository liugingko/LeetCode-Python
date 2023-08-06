# 方法 2
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m  # 保持 n 始终大于 m
        if n == 0:
            return None

        imin, imax, half_len = 0, m, int((m + n + 1) / 2)
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            # 确定 i j 两个值
            if i < m and nums2[j - 1] > nums1[i]:  # 现在说名 i 太小，应该增加
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:  # 现在说名 i 太大，应该减小
                imax = i - 1

            else:
                # i 的值已经确定，现在找中间值

                if i == 0:  # 确定左边界情况
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:  # 奇数的情况下
                    return max_of_left

                if i == m:  # 确定右边界情况
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    nums1, nums2 = [1, 3], [3, 4]
    solu = Solution()
    print(solu.findMedianSortedArrays(nums1, nums2))
