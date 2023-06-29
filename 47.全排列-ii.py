#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def assimble(queue,blocks):
            res = []
            if len(blocks)==1:
                res.append(queue+blocks)
            else:
                for i,j in enumerate(blocks):
                    res+=assimble(queue+[j],blocks[:i]+blocks[i+1:])
            return res
        tres = assimble([],nums)
        tres.sort()
        res = [tres[0]]
        for i in tres:
            if i!=res[-1]:
                res+=[i]
        return res
# @lc code=end

