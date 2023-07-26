#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        N = list(str(N))
        size = len(N)
        p = len(N)
        for i in range(size-1, 0, -1):
            if N[i] < N[i - 1]:
                N[i - 1] = str(int(N[i - 1])-1)
                p = i
        res = 0
        for i in range(len(N)):
            if i < p:
                res = res * 10 + int(N[i])
            else:
                res = res * 10 + 9
        return res
# @lc code=end

