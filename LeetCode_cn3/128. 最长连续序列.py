class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:

                curr_num = num
                curr_cnt = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_cnt += 1

                longest_streak = max(longest_streak, curr_cnt)

        return longest_streak