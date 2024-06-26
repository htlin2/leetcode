/**
 * @param {string[][]} accounts
 * @return {string[][]}
 */
var accountsMerge = function(accounts) {
    const emailIndex = {} // email: [1, 2, 3]
    accounts.forEach((a, i) => {
        for (const email of a.slice(1)) {
            if (email in emailIndex) {
                emailIndex[email].push(i)
            } else {
                emailIndex[email] = [i]
            }
        }
    })
    const visited = new Set()
    function dfs(i, emailSet) {
        if (i in visited) return
        visited.add(i)
        const account = accounts[i]
        for (const email of account.slice(1)) {
            emailSet.add(email)
            for (const nei of emailIndex[email]) {
                if (visited.has(nei)) continue
                dfs(nei, emailSet)
            }
        }
    }

    const res = []
    accounts.forEach((a, i) => {
        if (visited.has(i)) return
        const name = a[0]
        const emailSet = new Set()
        dfs(i, emailSet)
        const emails = [...emailSet].sort()
        res.push([name, ...emails])
    })
    return res
};