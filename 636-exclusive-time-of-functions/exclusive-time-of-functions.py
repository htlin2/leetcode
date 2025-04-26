class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        N = len(logs)
        for i in range(N):
            fn, fn_type, fn_time = logs[i].split(':')
            fn = int(fn)
            fn_time = int(fn_time)
            if not stack:
                stack.append(fn)
            elif fn_type == 'start':
                prev_fn = stack[-1]
                res[prev_fn] += fn_time - prev_time - 1
                stack.append(fn)
            elif fn_type == 'end':
                prev_fn = stack.pop()
                res[prev_fn] += fn_time - prev_time + 1
            prev_time = fn_time
        return res