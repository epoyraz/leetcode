class Solution(object):
    def findAnswer(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[bool]
        """
        n = len(parent)
        # build adjacency list of children and sort
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)
        for ch in children:
            ch.sort()
        # iterative post-order traversal
        post = []
        stack = [(0, False)]
        while stack:
            u, visited = stack.pop()
            if visited:
                post.append(u)
            else:
                stack.append((u, True))
                for v in reversed(children[u]):
                    stack.append((v, False))
        # compute subtree sizes using post-order
        size = [0] * n
        for u in post:
            total = 1
            for v in children[u]:
                total += size[v]
            size[u] = total
        # map each node to its position in post-order
        pos = [0] * n
        for idx, u in enumerate(post):
            pos[u] = idx
        # build the post-order string array
        T = [s[u] for u in post]
        # reverse string for backward hashing
        TR = T[::-1]
        # rolling hash parameters
        M = 10**9 + 7
        B = 29
        # precompute powers of B
        P = [1] * (n + 1)
        for i in range(1, n + 1):
            P[i] = (P[i-1] * B) % M
        # prefix hashes for T
        H = [0] * (n + 1)
        for i, ch in enumerate(T):
            H[i+1] = (H[i] * B + (ord(ch) - ord('a') + 1)) % M
        # prefix hashes for TR
        HR = [0] * (n + 1)
        for i, ch in enumerate(TR):
            HR[i+1] = (HR[i] * B + (ord(ch) - ord('a') + 1)) % M
        # compute answer for each node
        answer = [False] * n
        for u in range(n):
            r = pos[u]
            L = size[u]
            l = r - L + 1
            # forward hash on T[l..r]
            hf = (H[r+1] - H[l] * P[L] % M + M) % M
            # corresponding reversed segment in TR: indices [n-1-r .. n-1-l]
            L2 = n - 1 - r
            R2 = n - 1 - l
            hr = (HR[R2+1] - HR[L2] * P[L] % M + M) % M
            answer[u] = (hf == hr)
        return answer
