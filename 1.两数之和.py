#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        waitList = {}
        for i,j in enumerate(nums):
            if j in waitList:
                return([waitList[j], i])
            else:
                waitList[target-j] = i
# @lc code=end

