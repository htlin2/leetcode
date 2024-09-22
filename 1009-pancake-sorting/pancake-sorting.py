class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            arr[:end + 1] = arr[:end + 1][::-1]

        res = []
        N = len(arr)
        for i in range(N - 1, 0, -1):
            copy_arr = arr[:i+1]
            max_n = max(copy_arr)
            max_i = copy_arr.index(max_n)
            if max_i == i: continue
            if max_i != 0:
                flip(max_i)
                res.append(max_i + 1)
            flip(i)
            res.append(i + 1)
        return res
