class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        N = len(username)
        name_visit_map = collections.defaultdict(list)
        combs = data = sorted(zip(timestamp, username, website))
        for i in range(N):
            name = combs[i][1]
            visit = combs[i][2]
            name_visit_map[name].append(visit)
        res = collections.defaultdict(int)
        def dfs(visits, i, pattern, visited):
            if len(pattern) == 3:
                key = tuple(pattern)
                if key in visited: return
                res[key] += 1
                visited.add(key)
                return
            for j in range(i, len(visits)):
                pattern.append(visits[j])
                dfs(visits, j + 1, pattern, visited)
                pattern.pop()
        for name, visits in name_visit_map.items():
            dfs(visits, 0, [], set())
        tups = []
        max_count = max(res.values())
        for tup, count in res.items():
            if count == max_count:
                tups.append(tup)
        tups.sort(key=lambda x: (x[0], x[1], x[2]))
        return tups[0]
"""
Input: 
username =  ["joe","joe","joe","james","james","james","james","mary","mary","mary"], 
timestamp = [    1,    2,    3,      4,      5,      6,      7,     8,     9,   10], 
website =   ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]


["joe","home",1],
["joe","about",2],
["joe","career",3],
["james","home",4],
["james","cart",5],
["james","maps",6],
["james","home",7],
["mary","home",8],
["mary","about",9],
["mary","career",10].

backtracking + hashmap
name_visit_map
{
    joe: [home, about, career]
    james: [home, cart, maps, home]
    mary: [home, about, career]
}
run backtracking to find all tuple combinations
store tuples in a new hashmap

return highest count of tuple
"""