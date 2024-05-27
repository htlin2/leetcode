class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        email_index = collections.defaultdict(list)
        res = []
        for i, a in enumerate(accounts):
            for email in a[1:]:
                email_index[email].append(i)

        def dfs(i, emails):
            if i in visited: return
            visited.add(i)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for nei in email_index[email]:
                    dfs(nei, emails)
        
        for i, a in enumerate(accounts):
            if i in visited: continue
            name, emails = a[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res

"""
# emails_accounts_map of email to account ID
email_index = {
  "johnsmith@mail.com": [0, 2],
  "john00@mail.com": [0],
  "johnnybravo@mail.com": [1],
  "john_newyork@mail.com": [2],
  "mary@mail.com": [3]
}
"""