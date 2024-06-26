class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_index = collections.defaultdict(list)
        for i, a in enumerate(accounts):
            for email in a[1:]:
                email_index[email].append(i)
        
        visited = set()
        def dfs(i, emails):
            if i in visited: return
            visited.add(i)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for nei in email_index[email]:
                    if nei in visited: continue
                    dfs(nei, emails)

        res = []
        for i, a in enumerate(accounts):
            if i in visited: continue
            name = a[0]
            emails = set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
"""
[
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]
johnsmith@mail.com: [0, 1]
john_newyork@mail.com: [0]
john00@mail.com: [1]

"""