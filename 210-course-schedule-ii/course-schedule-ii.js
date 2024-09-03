/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(N, prerequisites) {
    const adj = {}
    for (let i = 0; i < N; i++) {
        adj[i] = []
    }
    for (const [req, crs] of prerequisites) {
        adj[req].push(crs)
    }
    const visited = new Set()
    function dfs(course, cycle) {
        if (visited.has(course)) return true;
        if (cycle.has(course)) return false;
        cycle.add(course);
        for (const nei of adj[course]) {
            if (!dfs(nei, cycle)) return false
        }
        visited.add(course)
        return true
    }

    for (let i = 0; i < N; i++) {
        if (!dfs(i, new Set())) return []
    }
    return visited.size === N ? [...visited] : []
};

`
numCourses = 2, prerequisites = [[1,0]]
                                req, 
output = [0, 1]


N = 4
[[1,0],[2,3], [1,0]]
output = [] -> cycle, canot complete

N = 4
[[1,0],[3,2],[3,1]]
0, 2 -> 1 -> 3
output = [0,2,1,3]
visited = {0, 1, 2, 3}
adj = toTake:req = {
    1: [0]
    3: [2, 1]
}

[[1,0],[2,0],[3,1],[3,2]]
visited = {0,1, 2, 3}
cycle = {}
adj = {
    1: [0]
    2: [0]
    3: [1, 2]
}
`