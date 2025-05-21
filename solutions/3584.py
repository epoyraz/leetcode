from bisect import bisect_left

class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)
        # Build position lists for each letter
        pos = [[] for _ in xrange(26)]
        for i, ch in enumerate(word1):
            pos[ord(ch) - 97].append(i)

        # Build nextDiffPos[i] = smallest j > i with word1[j] != word1[i], or n if none.
        nextDiff = [0] * n
        nextDiff[-1] = n
        for i in xrange(n-2, -1, -1):
            if word1[i] == word1[i+1]:
                nextDiff[i] = nextDiff[i+1]
            else:
                nextDiff[i] = i+1

        # 1) Greedy forward match (exact) to get A_prefix and P = how many we matched
        A = []
        last = -1
        for j in xrange(m):
            c = ord(word2[j]) - 97
            lst = pos[c]
            idx = bisect_left(lst, last+1)
            if idx == len(lst):
                break
            last = lst[idx]
            A.append(last)
        P = len(A)
        fullMatch = (P == m)

        # 2) Greedy backward to build L[j] = largest index in word1 where
        #    word2[j] can be matched so that the suffix j..m-1 is matchable.
        L = [0] * m
        # For j = m-1:
        c = ord(word2[m-1]) - 97
        if pos[c]:
            L[m-1] = pos[c][-1]
        else:
            L[m-1] = -1
        # Backward
        for j in xrange(m-2, -1, -1):
            c = ord(word2[j]) - 97
            if L[j+1] < 0:
                L[j] = -1
            else:
                lst = pos[c]
                # find largest < L[j+1]
                idx = bisect_left(lst, L[j+1]) - 1
                L[j] = lst[idx] if idx >= 0 else -1

        # 3) Try to find the earliest k where a mismatch at k yields a lexicographically smaller (or any) valid seq.
        #    k runs from 0..k_max = (fullMatch ? m-1 : P)
        k_max = (m-1) if fullMatch else P
        chosen_k = -1
        chosen_p = -1

        for k in xrange(k_max+1):
            last_idx = A[k-1] if k > 0 else -1
            s = last_idx + 1
            if s >= n:
                continue
            # find p = first pos >= s where word1[p] != word2[k]
            if word1[s] != word2[k]:
                p = s
            else:
                p = nextDiff[s]
            if p >= n:
                continue
            # suffix viability
            if k < m-1:
                if L[k+1] < 0 or p+1 > L[k+1]:
                    continue
            # if we have a full exact match, we only switch if this gives lexicographically smaller:
            if not fullMatch or p < A[k]:
                chosen_k, chosen_p = k, p
                break

        # 4) Build the answer
        if chosen_k == -1:
            # never found a beneficial (or any, if exact failed) mismatch
            return A if fullMatch else []

        # build S_k
        ans = [0] * m
        # prefix matches
        for j in xrange(chosen_k):
            ans[j] = A[j]
        # the mismatch
        ans[chosen_k] = chosen_p
        # the suffix matches
        last = chosen_p
        for j in xrange(chosen_k+1, m):
            c = ord(word2[j]) - 97
            lst = pos[c]
            idx = bisect_left(lst, last+1)
            # (we know it must exist because of our suffix check)
            last = lst[idx]
            ans[j] = last

        return ans
