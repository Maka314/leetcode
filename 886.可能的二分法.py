#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for x, y in dislikes:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)
        color = [0] * n  # color[x] = 0 表示未访问节点 x

        def dfs(x: int, c: int) -> bool:
            color[x] = c
            return all(color[y] != c and (color[y] or dfs(y, -c)) for y in g[x])
        
        return all(c or dfs(i, 1) for i, c in enumerate(color))
                
# @lc code=end

