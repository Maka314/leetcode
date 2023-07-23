#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res, i = 1, 1
        while i<len(nums) and nums[i] == nums[i - 1]:
            i += 1
        
        if i < len(nums) and nums[i] > nums[0]:
            expBig = True
        else:
            expBig = False

        for j in range(i,len(nums)):
            if expBig and nums[j] > nums[j - 1]:
                res += 1
                expBig = False
            elif not expBig and nums[j] < nums[j - 1]:
                res += 1
                expBig = True
        return res
# @lc code=end

