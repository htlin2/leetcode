/**
 * @param {string[][]} accounts
 * @return {string[][]}
 */
class UnionFind {
    constructor(N) {
        this.parents = Array(N).fill(1).map((e, idx) => idx)
        this.ranks = Array(N).fill(1)
    }
    
    find(n) {
        if (this.parents[n] === n) return n
        this.parents[n] = this.find(this.parents[this.parents[n]])
        return this.parents[n]
    }

    union(n1, n2) {
        const [p1, p2] = [this.find(n1), this.find(n2)]
        if (p1 === p2) return false
        if (this.ranks[p1] >= this.ranks[p2]) {
            this.ranks[p1] += this.ranks[p2]
            this.parents[p2] = p1
        } else {
            this.ranks[p2] += this.ranks[p1]
            this.parents[p1] = p2
        }
        return true
    }
}
var accountsMerge = function(accounts) {
    const emailToIdx = {} // email: accountIdx
    const uf = new UnionFind(accounts.length)
    accounts.forEach((account, idx) => {
        const emails = account.slice(1)
        emails.forEach(email => {
            if (email in emailToIdx) {
                uf.union(idx, emailToIdx[email])
            }
            emailToIdx[email] = uf.find(idx)
        })
    })

    const parentIdxToIndices = {} // parentIdx: [idx1, idx2]
    accounts.forEach((account, idx) => {
        const parentIdx = uf.find(idx)
        if (!(parentIdx in parentIdxToIndices)) {
            parentIdxToIndices[parentIdx] = new Set()
        }
        parentIdxToIndices[parentIdx].add(idx)
    })
    
    const res = []
    for (const [parentIdx, indices] of Object.entries(parentIdxToIndices)) {
        const account = accounts[Number(parentIdx)]
        const name = account[0]
        const emails = []
        for (const idx of indices) {
            const childAccount = accounts[idx].slice(1)
            emails.push(...childAccount)
        }
        const uniqueEmails = new Set(emails)
        const sortEmailAccounts = [...uniqueEmails]
        sortEmailAccounts.sort()
        res.push([name, ...sortEmailAccounts])
    }
    return res
};