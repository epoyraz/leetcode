class Solution(object):
    def exclusiveTime(self, n, logs):
        res = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)
            if typ == 'start':
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        
        return res
