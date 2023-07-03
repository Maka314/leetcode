#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)
        if not size:
            return [newInterval]
        r, l = 0, size-1
        while r<size and intervals[r][1]<newInterval[0]:
            r+=1
        while l>-1 and intervals[l][0]>newInterval[1]:
            l-=1
        if r==size:
            lower = newInterval[0]
        else:
            lower = min(intervals[r][0],newInterval[0])
        if l==-1:
            upper = newInterval[1]
        else:
            upper = max(intervals[l][1],newInterval[1])
        return(intervals[:r] + 
               [[lower , upper]] + 
               intervals[l+1:])
# @lc code=end

