import array
from collections import deque

class Solution(object):
    def minimumCost(self, target, words, costs):
        """
        :type target: str
        :type words: List[str]
        :type costs: List[int]
        :rtype: int
        """
        # 1) Deduplicate words, keeping only the minimal cost
        best = {}
        for w, c in zip(words, costs):
            if w in best:
                if c < best[w]:
                    best[w] = c
            else:
                best[w] = c

        # 2) Build AhoâCorasick trie of the unique words
        # children[node][ci] = next state for char ci (0..25)
        children = []
        fail     = array.array('I', [])    # failure link per node
        output   = []                       # output[node] = list of (length, cost)

        # initialize root
        children.append(array.array('I', [0]*26))
        fail.append(0)
        output.append([])

        # insert each word
        for w, c in best.items():
            node = 0
            for ch in w:
                ci = ord(ch) - ord('a')
                nxt = children[node][ci]
                if nxt == 0:
                    nxt = len(children)
                    children.append(array.array('I', [0]*26))
                    fail.append(0)
                    output.append([])
                    children[node][ci] = nxt
                node = nxt
            # mark end: store (word_length, cost)
            output[node].append((len(w), c))

        # 3) Build failure links and complete the goto table
        q = deque()
        # Depthâ1: link children of root back to root
        for ci in range(26):
            nxt = children[0][ci]
            if nxt:
                fail[nxt] = 0
                q.append(nxt)
            else:
                # missing edge => stay at root
                children[0][ci] = 0

        # BFS
        while q:
            r = q.popleft()
            for ci in range(26):
                u = children[r][ci]
                if u:
                    # set failure[u] = children[ fail[r] ][ci]
                    f = fail[r]
                    fci = children[f][ci]
                    fail[u] = fci
                    # merge outputs
                    output[u].extend(output[fci])
                    q.append(u)
                else:
                    # fill missing transition
                    children[r][ci] = children[fail[r]][ci]

        # 4) DP over prefixes of target
        n = len(target)
        INF = 10**30
        dp = [INF] * (n+1)
        dp[0] = 0

        node = 0
        for i, ch in enumerate(target, start=1):
            ci = ord(ch) - ord('a')
            node = children[node][ci]
            # for every word ending here
            for length, c in output[node]:
                prev = dp[i - length]
                if prev + c < dp[i]:
                    dp[i] = prev + c

        return dp[n] if dp[n] < INF else -1
