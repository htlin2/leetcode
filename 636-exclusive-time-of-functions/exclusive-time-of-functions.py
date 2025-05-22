class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        for i in range(len(logs)):
            func, type_, end_time = logs[i].split(':')
            func, end_time = int(func), int(end_time)
            if type_ == 'start':
                if stack:
                    res[stack[-1]] += end_time - prev_time
                stack.append(func)
                prev_time = end_time
            elif type_ == 'end':
                stack.pop()
                res[func] += end_time - prev_time + 1
                prev_time = end_time + 1
        return res