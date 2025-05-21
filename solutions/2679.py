class Solution:
    def distinctIntegers(self, n):
        visited = set()
        stack = [n]

        while stack:
            x = stack.pop()
            if x in visited:
                continue
            visited.add(x)
            for i in range(1, n + 1):
                if x % i == 1 and i not in visited:
                    stack.append(i)

        return len(visited)
