class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj = collections.defaultdict(set) # stop: [bus1, bus2]
        for i in range(len(routes)):
            for stop in routes[i]:
                adj[stop].add(i)
        q = collections.deque([source])
        visited_bus = set()
        visited_stop = set([source])
        count = 0
        while q:
            for _ in range(len(q)):
                stop = q.popleft()
                if stop == target: return count
                for next_bus in adj[stop]:
                    if next_bus in visited_bus: continue
                    visited_bus.add(next_bus)
                    for next_stop in routes[next_bus]:
                        if next_stop in visited_stop: continue
                        visited_stop.add(next_stop)
                        q.append(next_stop)
            count += 1
        return -1