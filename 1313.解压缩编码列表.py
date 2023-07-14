#
# @lc app=leetcode.cn id=1313 lang=python3
#
# [1313] 解压缩编码列表
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        size = len(nums)
        for i in range(0,size,2):
            res += [nums[i+1]]*nums[i]
        return res
# @lc code=end

