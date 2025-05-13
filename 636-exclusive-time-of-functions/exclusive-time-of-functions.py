class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        prev_time = 0
        stack = []
        for log in logs:
            idx, log_type, log_time = log.split(':')
            idx = int(idx)
            log_time = int(log_time)
            if log_type == 'start':
                if stack:
                    res[stack[-1]] += log_time - prev_time
                stack.append(idx)
                prev_time = log_time
            else:
                res[stack.pop()] += log_time - prev_time + 1
                prev_time = log_time + 1
        return res