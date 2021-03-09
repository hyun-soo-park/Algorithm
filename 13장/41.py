#https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = [[] for _ in range(n)]
        for i in flights:
            graph[i[0]].append((i[1], i[2]))

        q = []
        heapq.heappush(q, (0, src, K))

        while q:
            price, now, k = heapq.heappop(q)
            if now == dst:
                return price
            if k >= 0:
                for i in graph[now]:
                    heapq.heappush(q, (price + i[1], i[0], k - 1))

        return -1