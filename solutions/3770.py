class Solution(object):
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        L = n + m - 1

        # 1) initialize word with None, then apply all 'T' constraints
        word = [None]*L
        for i, ch in enumerate(str1):
            if ch == 'T':
                for j, c in enumerate(str2):
                    pos = i + j
                    if word[pos] is None:
                        word[pos] = c
                    elif word[pos] != c:
                        return ""  # conflict

        # 2) collect all F-window starts
        Fstarts = [i for i,ch in enumerate(str1) if ch=='F']

        # 3) for each F-window, compute initial blanks & mismatch
        blanks   = {}
        mismatch = {}
        for i in Fstarts:
            b = 0
            mm = 0
            for j in range(m):
                c = word[i+j]
                if c is None:
                    b += 1
                elif c != str2[j]:
                    mm += 1
            # if fully forced match, impossible
            if b == 0 and mm == 0:
                return ""
            blanks[i], mismatch[i] = b, mm

        # 4) precompute windows_of_pos
        windows_of_pos = [[] for _ in range(L)]
        for i in Fstarts:
            for j in range(m):
                windows_of_pos[i+j].append(i)

        # 5) greedy fill remaining positions
        for p in range(L):
            if word[p] is not None:
                continue
            for c in "abcdefghijklmnopqrstuvwxyz":
                bad = False
                # test c for every F-window covering p
                for i in windows_of_pos[p]:
                    b = blanks[i]
                    mm = mismatch[i]
                    # if we would place c==str2[p-i] then we'd reduce blanks by 1
                    # and mismatch stays mm.  If that leaves b-1==0 and mm==0, full match!
                    if c == str2[p - i] and b == 1 and mm == 0:
                        bad = True
                        break
                if not bad:
                    # accept c
                    word[p] = c
                    for i in windows_of_pos[p]:
                        # update that window's blanks & mismatch
                        if c == str2[p - i]:
                            blanks[i] -= 1
                        else:
                            blanks[i] -= 1
                            mismatch[i] += 1
                    break
            else:
                # no letter worked
                return ""

        # 6) final check (should already pass)
        for i in Fstarts:
            if blanks[i] == 0 and mismatch[i] == 0:
                return ""

        return "".join(word)
