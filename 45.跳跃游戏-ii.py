#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        route = [10000 for _ in range(len(nums))]
        route[-1]=0
        for i in range(len(nums)-2,-1,-1):#-2时从倒数第一个开始遍历
            if nums[i]:
                route[i] = 1+min(route[1+i:1+i+nums[i]])
        return route[0]
# @lc code=end

