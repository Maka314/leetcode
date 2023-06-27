#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def assimble(used, target):
            res = []
            for i in candidates:
                if i<target:
                    res+=assimble(used+[i],target-i)
                elif i==target:
                    temp = used+[i]
                    temp.sort() 
                    res+=[temp]
            return res
        tempRes = assimble([],target)
        res = []
        for r in tempRes:
            if r not in res:
                res.append(r)
        return res
# @lc code=end

