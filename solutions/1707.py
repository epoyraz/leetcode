class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if len(t) != n:
            return False

        # record positions of each digit 0..9 in s
        positions = [[] for _ in range(10)]
        for i, ch in enumerate(s):
            positions[ord(ch) - ord('0')].append(i)

        # pointers into each positions[d]: next alive occurrence
        head = [0] * 10
        removed = [False] * n

        # try to match t[k] one by one
        for ch in t:
            d = ord(ch) - ord('0')

            # skip over any already-removed positions for digit d
            while head[d] < len(positions[d]) and removed[positions[d][head[d]]]:
                head[d] += 1
            if head[d] == len(positions[d]):
                # no more of digit d to place
                return False

            pos = positions[d][head[d]]

            # check smaller digits e < d: none may lie alive to the left of pos
            for e in range(d):
                while head[e] < len(positions[e]) and removed[positions[e][head[e]]]:
                    head[e] += 1
                if head[e] < len(positions[e]) and positions[e][head[e]] < pos:
                    return False

            # remove this occurrence of d
            removed[pos] = True
            head[d] += 1

        return True
