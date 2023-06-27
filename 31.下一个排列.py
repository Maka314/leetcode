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
        '''
        从后向前遍历，只要出现某一个元素小于后面元素的情况，这个排列就能找到下一个
        再从后面寻找可能交换的元素，要求为大于该元素，但是是尾部元素中的最大值
        完成后，为了保证这个排列是最小排列，需要对后面的元素进行排序
        '''
        isBig = True
        for i1 in range(len(nums)-2,-1,-1):
            if nums[i1]<nums[i1+1]:
                #从i+1往后寻找稍微大一点的元素
                tempi = i1+1
                for i2 in range(i1+1,len(nums)):
                    if nums[i2]<nums[tempi] and nums[i2]>nums[i1]:
                        tempi = i2
                
                nums[i1],nums[tempi] = nums[tempi],nums[i1]
                isBig = False
                break
        
        if isBig:
            l = len(nums)
            for i,j in enumerate(nums):
                nums[-(i+1)],nums[i] = j ,nums[-(i+1)]
                if i+1>=l/2:
                    break
        else:
            tail = nums[i1+1:]
            tail.sort()
            for i3 in range(i1+1,len(nums)):
                nums[i3] = tail[i3-i1-1]

# @lc code=end

