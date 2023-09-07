#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislikes.sort()
        graph = [-1 for i in range(n)]
        hateList = [{} for i in range(1, n+1)]
        for dis in dislikes:
            hateList[dis[0] - 1].add(dis[1])
            hateList[dis[1] - 1].add(dis[1])
        
# @lc code=end

