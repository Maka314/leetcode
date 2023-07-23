#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.ticketBook = {}
        self.res = []
        ticketCount = len(tickets)
        for ticket in tickets:
            if ticket[0] in self.ticketBook:
                self.ticketBook[ticket[0]].append([ticket[1], 1])
            else:
                self.ticketBook[ticket[0]] = [[ticket[1], 1]]
        for startP in self.ticketBook:
            self.ticketBook[startP].sort(reverse = True)
        print(self.ticketBook)
    
    def backTracking(self,currentAirport, ticketCount):
        for t in self.ticketBook[currentAirport]:
            


# @lc code=end

