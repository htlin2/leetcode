class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        res = []
        for i in range(0, N - 2):
            for j in range(i + 1, N - 1):
                abs_a = abs(arr[i] - arr[j])
                if abs_a > a: continue
                for k in range(j + 1, N):
                    abs_b = abs(arr[j] - arr[k])
                    if abs_b > b: continue
                    abs_c = abs(arr[i] - arr[k])
                    if abs_c > c: continue
                    res.append((arr[i], arr[j], arr[k]))
        return len(res)