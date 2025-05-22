class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj = collections.defaultdict(set) # stop: bus[]
        for bus, route in enumerate(routes):
            for stop in route:
                adj[stop].add(bus)
        if source == target: return 0
        if source not in adj or target not in adj: return -1
        res = 0
        q = collections.deque([source])
        visited_stop = set([source])
        visited_bus = set()
        while q:
            for _ in range(len(q)):
                stop = q.popleft()
                if stop == target: return res
                for next_bus in adj[stop]:
                    if next_bus in visited_bus: continue
                    visited_bus.add(next_bus)
                    for next_stop in routes[next_bus]:
                        if next_stop in visited_stop: continue
                        visited_stop.add(next_stop)
                        q.append(next_stop)
            res += 1
        return -1