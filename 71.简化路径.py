#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        fileRoute = []
        path+="/"
        length = len(path)
        for i in range(length):
            if path[i]=="/":
                if fileRoute and fileRoute[-1]=="..":
                    if len(fileRoute)==1:
                        fileRoute=[]
                    else:
                        fileRoute=fileRoute[:-2]
                if fileRoute and fileRoute[-1]==".":
                    fileRoute = fileRoute[:-1]
            elif path[i-1] == "/":
                fileRoute.append(path[i])
            else:
                fileRoute[-1]+=path[i]
        return "/"+"/".join(fileRoute)
# @lc code=end

