#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        chartCount = {0:0,
                      1:0,
                      2:0}
        for i in nums:
            chartCount[i] += 1

        for i in range(chartCount[0]):
            p = self.findNext(nums,i,0)
            nums[i], nums[p] = nums[p], nums[i]
        for i in range(chartCount[0],chartCount[0]+chartCount[1]):
            p = self.findNext(nums,i,1)
            nums[i], nums[p] = nums[p], nums[i]
        for i in range(chartCount[0]+chartCount[1],len(nums)):
            p = self.findNext(nums,i,2)
            nums[i], nums[p] = nums[p], nums[i]
    
    def findNext(self, nums, start, target):
        for i in range(start,len(nums)):
            if nums[i] == target:
                return i
# @lc code=end

