#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def assimble(candidates, used, target):
            res = []
            print()
            for i,j in enumerate(candidates):
                if j<target:
                    res+=assimble(candidates[:i] + candidates[i+1:],used+[j],target-j)
                elif j==target:
                    temp = used+[j]
                    temp.sort()
                    res+=[temp]
            return res
        tempRes = assimble(candidates,[],target)
        res = []
        for r in tempRes:
            if r not in res:
                res.append(r)
        return res
# @lc code=end

