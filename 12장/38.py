#https://leetcode.com/problems/reconstruct-itinerary/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []

        def dfs(start, path, visit):
            if len(path) == len(tickets) + 1:
                result.append(path)
                return
            visit.append(start)
            for i in range(len(tickets)):
                if path[-1] == tickets[i][0] and not i in visit:
                    dfs(i, path + [tickets[i][1]], visit)

        for j in range(len(tickets)):
            visit = []
            dfs(j, tickets[j], visit)

        result.sort()
        return result[0]
