#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        iF, iS, iN = 0, 0, 0
        size = len(chars)

        while iF < size:
            if chars[iF] == chars[iS]:
                iF += 1
            elif iF == iS+1:
                iN += 1
                chars[iN] = chars[iF]
                iS += 1
                iF += 1
            else:
                iN += 1
                count = str(iF - iS)
                for c in count:
                    chars[iN] = c
                    iN += 1
                iS = iF
                chars[iN] = chars[iS]
                iF += 1
        if iF == iS+1:
            iN += 1
            if iN < size:
                chars[iN] = chars[iS]
        else:
            iN += 1
            count = str(iF - iS)
            for c in count:
                chars[iN] = c
                iN += 1
        return iN
# @lc code=end

