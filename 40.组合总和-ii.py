#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        self.trackBacking(candidates, 0, [], 0, target)
        return self.res

    def trackBacking(self, candidates, startIndex, track, trackSum, target):
        if trackSum == target:
            self.res.append(track[:])
            return

        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i-1]:
                continue #同样关键的优化
                
            if trackSum + candidates[i] > target:
                break #关键优化

            track.append(candidates[i])
            trackSum += candidates[i]
            self.trackBacking(candidates, i + 1, track, trackSum, target)
            trackSum -= candidates[i]
            track.pop()


# @lc code=end
