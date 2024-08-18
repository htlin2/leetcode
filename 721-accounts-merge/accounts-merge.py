class UnionFind:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.ranks = [1] * N

    def find(self, n):
        if self.parents[n] == n: return n
        self.parents[n] = self.find(self.parents[self.parents[n]])
        return self.parents[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False
        if self.ranks[p1] >= self.ranks[p2]:
            self.ranks[p1] += self.ranks[p2]
            self.parents[p2] = p1
        else:
            self.ranks[p2] += self.ranks[p1]
            self.parents[p1] = p2
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        uf = UnionFind(N)
        email_idx = {}
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email in email_idx:
                    uf.union(i, email_idx[email])
                else:
                    email_idx[email] = i
        parent_emails = collections.defaultdict(list)
        for e, i in email_idx.items():
            parent = uf.find(i)
            parent_emails[parent].append(e)
        res = []
        for i, emails in parent_emails.items():
            name = accounts[i][0]
            name_emails = [name] + sorted(emails)
            res.append(name_emails)
        return res
            
"""
dfs
johnsmith@mail.com: 0
john_newyork@mail.com: 0
john00@mail.com: 1
mary@mail.com: 2
johnnybravo@mail.com: 3

0: [johnsmith@mail.com, john_newyork@mail.com]
1: [john00@mail.com]


"""