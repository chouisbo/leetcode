#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        def validContinuousSame(nums:list[int], startPos:int, length:int):
            if (startPos < 0) or ((startPos+length) > len(nums)):
                return False
            for i in range(1, length):
                if nums[startPos + i] != nums[startPos]:
                    return False
            return True

        def validSeq1(nums:list[int], startPos:int, length: int):
            if (startPos < 0) or ((startPos+length) > len(nums)):
                return False
            value = nums[startPos]
            for i in range(1, length):
                if nums[startPos + i] != (value+1):
                    return False
                value += 1
            return True

        N = len(nums)
        if N < 2: return False

        dp = [False] * N
        # dp[n] 表示 nums[n:] 这个子数组是否可以正确划分
        invalid = True
        if N >= 2 and validContinuousSame(nums, N-2, 2):
            dp[N-2] = True
            invalid = False
            if 2 == N: return not invalid
        if N >= 3 and validContinuousSame(nums, N-3, 3):
            dp[N-3] = True
        if N >= 3 and validSeq1(nums, N-3, 3):
            dp[N-3] = True

        for i in range(N-4, -1, -1):
            if dp[i+2]:
                if validContinuousSame(nums, i, 2):
                    dp[i] = True
                    continue
            if dp[i+3]:
                if validContinuousSame(nums, i, 3) or validSeq1(nums, i, 3):
                    dp[i] = True
                    continue
        return dp[0]



if __name__ == "__main__":
    s = Solution()
    print(s.validPartition([4,4,4,5,6]))
    print(s.validPartition([1,1,1,2]))
    print(s.validPartition([1,3,3]))





