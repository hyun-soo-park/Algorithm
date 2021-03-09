#https://leetcode.com/problems/network-delay-time/submissions/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = 1e9
        distance = [inf for _ in range(n+1)]
        graph = [[] for _ in range(n+1)]
        for i in times:
            graph[i[0]].append((i[1],i[2]))

        q = []
        visit = [False] * (n+1)
        distance[k] = 0
        heapq.heappush(q,(0,k))

        while q:
            dt,now = heapq.heappop(q)
            visit[now] = True
            for i in graph[now]:
                if dt + i[1] < distance[i[0]] and visit[i[0]]==False:
                    distance[i[0]] = dt + i[1]
                    heapq.heappush(q,(distance[i[0]],i[0]))

        if max(distance[1:]) == inf:
            return -1
        else:
            return max(distance[1:])