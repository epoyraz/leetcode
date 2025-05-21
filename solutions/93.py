class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return

            for l in range(1, 4):
                if start + l > len(s):
                    break
                segment = s[start:start+l]
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(start + l, path + [segment])

        backtrack(0, [])
        return res
