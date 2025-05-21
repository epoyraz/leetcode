class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        parent = [i for i in range(26)]  # one for each lowercase letter

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            # always attach the larger root to the smaller one (lex order)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        result = []
        for ch in baseStr:
            smallest = find(ord(ch) - ord('a'))
            result.append(chr(smallest + ord('a')))

        return ''.join(result)
