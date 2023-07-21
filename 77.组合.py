#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        useable = [i for i in range(1, n + 1)]
        return self.backTrack(useable, k)

    def backTrack(self, useable, k):
        if k == 1:
            res = [[i] for i in useable]
            return res
        else:
            res = []
            for i in range(len(useable) - k + 1):
                tempR = self.backTrack(useable[i + 1 :], k - 1)
                for r in tempR:
                    res += [[useable[i]] + r]
            return res


# @lc code=end
