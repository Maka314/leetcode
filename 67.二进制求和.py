#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def btten(s):
            res = 0
            for i,j in enumerate(s[::-1]):
                res+=(int(j)*2**(i))
            return res
        def tentb(n):
            if not n:
                return '0'
            d = 0
            res = ''
            while 2**d<=n:
                d+=1
            for i in range(d-1,-1,-1):
                if 2**i<=n:
                    n-=2**i
                    res+='1'
                else:
                    res+='0'
            return res
        return(tentb(btten(a)+btten(b)))
# @lc code=end

