class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        res = 0
        for i in range(0, N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    abs_a = abs(arr[i] - arr[j])
                    abs_b = abs(arr[j] - arr[k])
                    abs_c = abs(arr[i] - arr[k])
                    if abs_a <= a and abs_b <= b and abs_c <= c:
                        res += 1
        return res