class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = [] # fun
        curr_time = 0
        for log in logs:
            fn, _type, _time = log.split(':')
            fn, _time = int(fn), int(_time)
            if _type == 'start':
                if stack:
                    res[stack[-1]] += _time - curr_time
                stack.append(fn)
                curr_time = _time
            else:
                if stack:
                    stack.pop()
                res[fn] += _time - curr_time + 1
                curr_time = _time + 1
        return res
"""
stack
"""