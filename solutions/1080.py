class Solution:
    def camelMatch(self, queries, pattern):
        def matches(query):
            p = 0
            for c in query:
                if p < len(pattern) and c == pattern[p]:
                    p += 1
                elif c.isupper():
                    return False
            return p == len(pattern)

        return [matches(q) for q in queries]
