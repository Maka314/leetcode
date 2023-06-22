#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 10**4
        for i1,j1 in enumerate(nums[:-2]):
            if not i1 and j1==nums[i1-1]:
                continue
            #循环至倒数第三个元素
            roundT = target - j1
            l, r = i1+1, len(nums)-1
            while r > l:
                if nums[r]+nums[l]==roundT:
                    return(j1+nums[r]+nums[l])
                if abs(res-target)>abs(roundT-nums[r]-nums[l]):
                    res = j1+nums[r]+nums[l]
                if nums[r]+nums[l]>roundT:
                    r -= 1
                    while nums[r]==nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    while nums[l]==nums[l-1]:
                        l -= 1
            return res
# @lc code=end

