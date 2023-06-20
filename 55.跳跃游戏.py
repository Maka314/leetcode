#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums[-1]=-1
        for i in range(len(nums)-2,-1,-1):
            if -1 in nums[i+1:i+1+nums[i]]:
                nums[i]=-1
        if nums[0]==-1:
            return True
        else:
            return False

# @lc code=end

