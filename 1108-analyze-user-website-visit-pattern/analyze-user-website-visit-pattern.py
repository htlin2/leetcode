class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        N = len(username)
        data = sorted(zip(timestamp, username, website))
        name_visits = collections.defaultdict(list)
        for i in range(N):
            name = data[i][1]
            visit = data[i][2]
            name_visits[name].append(visit)

        pattern_count = collections.defaultdict(int)
        def dfs(visits, i, pattern, visited):
            if len(pattern) == 3:
                key = tuple(pattern)
                if key in visited: return
                visited.add(key)
                pattern_count[key] += 1
                return
            for j in range(i, len(visits)):
                pattern.append(visits[j])
                dfs(visits, j + 1, pattern, visited)
                pattern.pop()
            return
        for visits in name_visits.values():
            dfs(visits, 0, [], set())
        max_count = max(pattern_count.values())
        res = []
        for pattern, count in pattern_count.items():
            if count == max_count:
                res.append(pattern)
        res.sort()
        return res[0]

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