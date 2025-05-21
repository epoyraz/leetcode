class Solution(object):
    def countCompleteSubstrings(self, word, k):
        n = len(word)
        res = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and abs(ord(word[j]) - ord(word[j-1])) <= 2:
                j += 1
            m = j - i
            if m >= k:
                seg = word[i:j]
                for d in range(1, min(26, m // k) + 1):
                    L = d * k
                    arr = [0] * 26
                    distinct = exact = 0
                    for x in seg[:L]:
                        arr[ord(x)-97] += 1
                    for cnt in arr:
                        if cnt > 0: distinct += 1
                        if cnt == k: exact += 1
                    if distinct == exact == d:
                        res += 1
                    for s in range(1, m - L + 1):
                        r = ord(seg[s-1]) - 97
                        o = arr[r]
                        arr[r] = o - 1
                        if o == 1: distinct -= 1
                        if o == k: exact -= 1
                        if o == k+1: exact += 1
                        a = ord(seg[s+L-1]) - 97
                        o = arr[a]
                        arr[a] = o + 1
                        if o == 0: distinct += 1
                        if o == k-1: exact += 1
                        if o == k: exact -= 1
                        if distinct == exact == d:
                            res += 1
            i = j
        return res
