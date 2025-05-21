class Solution(object):
    def evaluate(self, s, knowledge):
        # build lookup dict
        km = {k: v for k, v in knowledge}
        res = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                # extract key until ')'
                j = i + 1
                while j < n and s[j] != ')':
                    j += 1
                key = s[i+1:j]
                # append value or '?' if missing
                res.append(km.get(key, '?'))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)
