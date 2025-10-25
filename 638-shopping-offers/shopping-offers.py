class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        N = len(price)
        good_specials = []
        for offer in special:
            bundle_cost = offer[-1]
            individual_cost = 0
            for i in range(N):
                individual_cost += offer[i] * price[i]
            if bundle_cost <= individual_cost:
                good_specials.append(offer)

        memo = {}
        def dfs(needs):
            if needs in memo:
                return memo[needs]
            best = sum([needs[i] * price[i] for i in range(N)])
            for offer in good_specials:
                nxt = []
                bundle_cost = offer[-1]
                is_valid = True
                for i in range(N):
                    if needs[i] < offer[i]:
                        is_valid = False
                        break
                    nxt.append(needs[i] - offer[i])
                if is_valid:
                    best = min(best, bundle_cost + dfs(tuple(nxt)))
            memo[needs] = best
            return best
        return dfs(tuple(needs))
"""
backtracking / dp


"""