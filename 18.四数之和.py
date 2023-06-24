#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        for i1,j1 in enumerate(nums[:-3]):
            if i1 and j1==nums[i1-1]:
                continue#跳过第一个重复元素
            for i2,j2 in enumerate(nums[i1+1:-2]):
                if i2 and j2==nums[i2+i1+1-1]:
                    continue#跳过第二个重复元素
                i3,i4 = i1+1+i2+1,len(nums)-1
                while i4>i3:
                    s=sum([j1,j2,nums[i3],nums[i4]])
                    if s==target:
                        res.append([j1,j2,nums[i3],nums[i4]])
                        #输出匹配成功的四个下标
                        print(i1,i2+i1+1,i3,i4)
                        i3+=1
                        while nums[i3]==nums[i3-1] and i3<i4:
                            i3+=1
                    elif s>target:
                        i4-=1
                        while nums[i4]==nums[i4+1] and i4>i3:
                            i4-=1
                    else:
                        i3+=1
                        while nums[i3]==nums[i3-1] and i3<i4:
                            i3+=1
        return res
# @lc code=end

