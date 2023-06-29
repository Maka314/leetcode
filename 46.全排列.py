#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def assimble(queue,blocks):
            res = []
            if len(blocks)==1:
                res.append(queue+blocks)
            else:
                for i,j in enumerate(blocks):
                    res+=assimble(queue+[j],blocks[:i]+blocks[i+1:])
            return res
        res = assimble([],nums)
        return res
# @lc code=end

