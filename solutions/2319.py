class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        size = 4 * n
        lchar = [0] * size
        rchar = [0] * size
        pref  = [0] * size
        suff  = [0] * size
        best  = [0] * size
        length = [0] * size

        def build(node, l, r):
            length[node] = r - l + 1
            if l == r:
                c = ord(s[l]) - 97
                lchar[node] = rchar[node] = c
                pref[node] = suff[node] = best[node] = 1
                return
            mid = (l + r) // 2
            left = node * 2
            right = left + 1
            build(left, l, mid)
            build(right, mid + 1, r)
            merge(node, left, right)

        def merge(node, left, right):
            lchar[node] = lchar[left]
            rchar[node] = rchar[right]
            pref[node] = pref[left]
            suff[node] = suff[right]
            best[node] = best[left] if best[left] > best[right] else best[right]
            if rchar[left] == lchar[right]:
                # combined run
                run = suff[left] + pref[right]
                if run > best[node]:
                    best[node] = run
                if pref[left] == length[left]:
                    pref[node] = length[left] + pref[right]
                if suff[right] == length[right]:
                    suff[node] = length[right] + suff[left]

        def update(node, l, r, idx, c):
            if l == r:
                lchar[node] = rchar[node] = c
                pref[node] = suff[node] = best[node] = 1
                return
            mid = (l + r) // 2
            left = node * 2
            right = left + 1
            if idx <= mid:
                update(left, l, mid, idx, c)
            else:
                update(right, mid + 1, r, idx, c)
            merge(node, left, right)

        build(1, 0, n - 1)
        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            c = ord(ch) - 97
            update(1, 0, n - 1, idx, c)
            res.append(best[1])
        return res
