class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = collections.defaultdict(list)
        for i, a in enumerate(accounts):
            for email in a[1:]:
                adj[email].append(i)
        visited = set()
        def dfs(idx, emails):
            if idx in visited: return
            visited.add(idx)
            for email in accounts[idx][1:]:
                emails.add(email)
                for nei in adj[email]:
                    dfs(nei, emails)

        res = []
        for i, a in enumerate(accounts):
            if i in visited: continue
            name, emails = a[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
            
"""
dfs
johnsmith@mail.com: [0]
john_newyork@mail.com: [0]
john00@mail.com: [0, 1]
mary@mail.com: [2]
johnnybravo@mail.com: [3]
"""