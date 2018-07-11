class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:return 0
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
        return i+1

    def removeDuplicates1(self, A):
        if not A:
            return 0
        else:
            ii,jj=1,1
            while jj<len(A):
                if A[ii-1]!=A[jj]:
                    A[ii]=A[jj]
                    ii+=1
                jj+=1
            return ii
        # A[:] = sorted(list(set(A)))
        # return len(A)
if __name__ == '__main__':
    solu = Solution()
    nums = [1,1,2]
    print(solu.removeDuplicates1(nums))