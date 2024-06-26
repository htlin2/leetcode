/**
 * @param {string[][]} accounts
 * @return {string[][]}
 */
class UnionFind {
    constructor(N) {
        this.parents = []
        this.ranks = []
        for (let i = 0; i < N; i++) {
            this.parents.push(i)
            this.ranks.push(1)
        }
    }
    find(n) {
        if (n === this.parents[n]) return n
        this.parents[n] = this.find(this.parents[this.parents[n]])
        return this.parents[n]
    }
    union(n1, n2) {
        const p1 = this.find(n1)
        const p2 = this.find(n2)
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
    const UF = new UnionFind(accounts.length)
    const email_index = {}
    accounts.forEach((a, i) => {
        for (let j = 1; j < a.length; j++) {
            const email = a[j]
            if (email in email_index) {
                UF.union(i, email_index[email])
            } else {
                email_index[email] = i
            }
        }
    })
    const index_emails = {}
    for (const [email, index] of Object.entries(email_index)) {
        parent = UF.find(index)
        if (!index_emails[parent]) {
            index_emails[parent] = [email]
            continue
        }
        index_emails[parent].push(email)
    }
    const res = []
    for (const [index, emails] of Object.entries(index_emails)) {
        const name = accounts[index][0]
        console.log(emails)
        emails.sort()
        res.push([name, ...emails])
    }
    return res
};