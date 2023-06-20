#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ci = 0
        res = [intervals[0]]
        for v in intervals:
            if v[0] <= res[ci][1]:
                res[ci][1] = max(v[1],res[ci][1])
                #需要合并
            else:
                ci+=1
                res.append(v)
        return res

# @lc code=end

