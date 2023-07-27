#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.slution = {
            0:1,
            1:1,
            2:2
        }

    def numTrees(self, n: int) -> int:
        if n in self.slution:
            return self.slution[n]
        res = 0
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n-1-i)
        self.slution[n] = res
        return res
# @lc code=end

