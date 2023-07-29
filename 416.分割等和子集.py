#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        if s % 2:
            return False
        
        #需要构建一个相当于一半容量的背包
        bag = [[0 for _ in range(s//2 + 1)] for _ in range(n)]

        #初始化第一行
        item = 0
        for compasity in range(s//2 + 1):
            if compasity >= nums[item]:
                bag[item][compasity] = nums[item]
        
        for item in range(1, len(nums)):
            for compasity in range(s//2 + 1):
                if compasity - nums[item] < 0:
                    #不能塞下这个和其他物品
                    bag[item][compasity] = bag[item - 1][compasity]
                else:
                    bag[item][compasity] = max(bag[item - 1][compasity], bag[item - 1][compasity - nums[item]] + nums[item], 0)

        return s//2 == bag[len(nums)-1][s//2]
# @lc code=end

