class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        str_x = str(abs(x))
        res = collections.deque([])
        for i in range(len(str_x) - 1, -1, -1):
            res.append(str_x[i])
        for i in range(len(res)):
            if res[i] == '0' and len(res) != len(str_x):
                res.popleft()
            else:
                break
        res_str = ''.join(res)
        res_int = int(res_str)
        if 2 ** 31 - 1 < res_int: return 0
        return -1 * res_int if is_negative else res_int