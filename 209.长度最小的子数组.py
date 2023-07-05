#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,s=0,0
        size = len(nums)
        res = size+1
        for r in range(size):
            s+=nums[r]
            while l<r and (s-nums[l])>=target:
                s-=nums[l]
                l+=1
            if s>=target:
                res = min(res,r-l+1)
        if res == size+1:
            res=0
        return res
# @lc code=end

