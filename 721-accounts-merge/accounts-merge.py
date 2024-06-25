class UF:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.ranks = [1] * N

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

    def find(self, n):
        if n == self.parents[n]: return n
        self.parents[n] = self.find(self.parents[self.parents[n]])
        return self.parents[n]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        uf = UF(N)
        email_index = {}
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email not in email_index:
                    email_index[email] = i
                else:
                    uf.union(i, email_index[email])
        index_emails = collections.defaultdict(list)
        for email, index in email_index.items():
            parent = uf.find(index)
            index_emails[parent].append(email)
        res = []
        for index, emails in index_emails.items():
            name = accounts[index][0]
            emails.sort()
            res.append([name, *emails])
        return res
"""
Union Find
[
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]
Union(0, 1)

email: account_index
johnsmith@mail.com: 0
john_newyork@mail.com: 0
john00@mail.com: 1
mary@mail.com: 2
johnnybravo@mail.com: 3

account_index: emails
0: [johnsmith@mail.com, john_newyork@mail.com, john00@mail.com]
2: [mary@gmail.com]
3: [john00@mail.com]

res = [
    [john, johnsmith@mail.com, john_newyork@mail.com, john00@mail.com]
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]
"""