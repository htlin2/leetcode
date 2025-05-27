class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        adj = collections.defaultdict(set)
        for i in range(len(recipes)):
            recipe = recipes[i]
            ingredient = ingredients[i]
            adj[recipe] = set(ingredient)
        
        def dfs(src, cycle):
            if src in supplies: return True
            if src in cycle: return False
            cycle.add(src)
            res = []
            for nei in adj[src]:
                res.append(dfs(nei, cycle))
            if not res or not all(res):
                return False
            supplies.add(src)
            return True
        
        res = []
        for src in adj.copy():
            if dfs(src, set()):
                res.append(src)
        return res

"""
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]

bread: ["yeast","flour"]
sandwich: ["bread","meat"]

"""