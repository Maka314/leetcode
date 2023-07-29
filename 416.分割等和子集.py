#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s//2
        
        #需要构建一个相当于一半容量的背包
        bag = [False for _ in range(target + 1)]
        bag[0] = True

        #逐个检查背包
        for item in range(len(nums)):
            for capacity in range(target, 0, -1):
                if capacity >= nums[item]:
                    bag[capacity] = bag[capacity] or bag[capacity - nums[item]]                    

            if bag[-1]:
                return True
        return False
# @lc code=end

