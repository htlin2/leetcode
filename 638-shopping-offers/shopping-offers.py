from typing import List, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        # 1) Keep only specials that are real discounts
        good = []
        for ofr in special:
            if ofr[-1] < sum(ofr[i] * price[i] for i in range(n)):
                good.append(ofr)

        memo = {}

        def min_cost_buy_individually(state: Tuple[int, ...]) -> int:
            return sum(state[i] * price[i] for i in range(n))

        def dfs(i: int, state: Tuple[int, ...]) -> int:
            key = (i, state)
            if key in memo:
                return memo[key]

            # If no more offers, finish by buying individually
            best = min_cost_buy_individually(state)
            if i == len(good):
                memo[key] = best
                return best

            offer = good[i]

            # Compute the maximum times we can take this offer
            # (bounded by remaining need per item)
            max_take = float('inf')
            for j in range(n):
                if offer[j] == 0: 
                    continue
                if offer[j] > state[j]:
                    max_take = 0  # cannot take even once
                    break
                max_take = min(max_take, state[j] // offer[j])
            if max_take == float('inf'):  # offer has no items; ignore it
                max_take = 0

            # Try k times taking this offer, then move to next offer
            # k = 0 is the "skip" branch
            cur_state = list(state)
            for k in range(0, max_take + 1):
                # Cost for taking k times of this offer + solve remaining with later offers
                cost_k = k * offer[-1] + dfs(i + 1, tuple(cur_state))
                if cost_k < best:
                    best = cost_k

                # Prepare state for next k+1 by subtracting one more offer
                for j in range(n):
                    cur_state[j] -= offer[j]
                    if cur_state[j] < 0:
                        break  # safeguard; though max_take prevents this

            memo[key] = best
            return best

        return dfs(0, tuple(needs))
