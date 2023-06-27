#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_i = len(nums)-1
        flag = True
        v = nums[-1]
        for i,j in enumerate(nums[::-1]):
            if i<max_i and nums[max_i-i-1]<v:
                for c in range(max_i,max_i-i-1,-1):
                    nums[c]=nums[c-1]
                nums[max_i-i-1]=v
                flag = False
                break
            elif nums[max_i-i-1]<j:
                nums[max_i-i] = nums[max_i-i-1]
                nums[max_i-i-1] = j
                flag = False
                break
        if flag:
            l = len(nums)
            for i,j in enumerate(nums):
                nums[-(i+1)],nums[i] = j ,nums[-(i+1)]
                if i+1>l/2:
                    break
# @lc code=end

