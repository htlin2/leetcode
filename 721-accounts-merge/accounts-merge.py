class UnionFind:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.ranks = [1] * N

    def find(self, n):
        if n == self.parents[n]: return n
        self.parents[n] = self.find(self.parents[self.parents[n]])
        return self.parents[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False
        if self.ranks[p1] >= self.ranks[p2]:
            self.ranks[p1] += self.ranks[p2]
            self.parents[p2] = self.parents[p1]
        else:
            self.ranks[p2] += self.ranks[p1]
            self.parents[p1] = self.parents[p2]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        UF = UnionFind(N)
        email_index = {}
        for i, a in enumerate(accounts):
            for email in a[1:]:
                if email not in email_index:
                    email_index[email] = i
                else:
                    UF.union(i, email_index[email])
        index_emails = collections.defaultdict(list)
        for email, index in email_index.items():
            parent = UF.find(index)
            index_emails[parent].append(email)
        ans = []
        for index, emails in index_emails.items():
            emails.sort()
            name = accounts[index][0]
            temp = [name] + emails
            ans.append(temp)
        return ans

"""
Union Find
account index = parents' index
email_index = {
    johnsmith@mail.com: 0,
    john_newyork@mail.com: 0,
    john00@mail.com: 0,
    mary@mail.com: 2,
    johnnybravo@mail.com: 3
}
index_emails = {
    0: [johnsmith@mail.com, john_newyork@mail.com, john00@mail.com],
    2: [mary@mail.com]
}
ans = []
['John', **sorted(index_emails[0])]
append above to ans
"""