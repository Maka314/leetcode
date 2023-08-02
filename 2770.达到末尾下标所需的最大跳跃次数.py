#
# @lc app=leetcode.cn id=2770 lang=python3
#
# [2770] 达到末尾下标所需的最大跳跃次数
#


# @lc code=start
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            maxStep = -1
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= target and res[j] > maxStep:
                    maxStep = res[j]
            if maxStep == -1:
                res[i] = -1
            else:
                res[i] = maxStep + 1
        return res[0]


# @lc code=end
