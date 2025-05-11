class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj = collections.defaultdict(set) # stop: route[]
        q = collections.deque([(source, 0)]) # [stop, count]
        for i in range(len(routes)):
            for stop in routes[i]:
                adj[stop].add(i)
        
        visited_route = set()
        visited_stop = set()
        visited_stop.add(source)
        while q:
            stop, count = q.popleft()
            if stop == target:
                return count
            for next_route in adj[stop]:
                if next_route in visited_route: continue
                visited_route.add(next_route)
                for next_stop in routes[next_route]:
                    if next_stop in visited_stop: continue
                    visited_stop.add(next_stop)
                    q.append((next_stop, count + 1))
        return -1
"""
source = 1, target = 6
routes = [
    [1,2,7],
    [3,6,7]
], 
Output: 2
1: [0]
2: [0]
3: [1]
6: [1]
7: [0,1]
"""