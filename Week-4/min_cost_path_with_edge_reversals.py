import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n, edges):
        # adjacency list: node -> list of (neighbor, weight)
        adj = defaultdict(list)

        for u, v, wt in edges:
            adj[u].append((v, wt))        # original direction
            adj[v].append((u, 2 * wt))    # reversed direction with double weight

        # Distance array
        dist = [float('inf')] * n
        dist[0] = 0

        # Min-heap: (current_distance, node)
        pq = [(0, 0)]

        while pq:
            d, node = heapq.heappop(pq)

            # If we already found a better path, skip
            if d > dist[node]:
                continue

            # If we reached destination
            if node == n - 1:
                return d

            for nei, wt in adj[node]:
                new_dist = d + wt
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))

        return -1
