class Solution(object):
    def smallestBeautifulString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        Returns the lexicographically smallest beautiful string > s, or "" if none.
        Beautiful: no palindrome substring length >=2.
        """
        n = len(s)
        s_list = list(s)
        # helper to check valid at pos i for char c
        def valid_at(i, c):
            if i > 0 and s_list[i-1] == c:
                return False
            if i > 1 and s_list[i-2] == c:
                return False
            return True

        # attempt position i from end
        for i in range(n-1, -1, -1):
            orig = s_list[i]
            # try next chars
            for code in range(ord(orig)+1, ord('a')+k):
                c = chr(code)
                if not valid_at(i, c):
                    continue
                # set prefix
                s_list[i] = c
                # fill suffix greedily
                for j in range(i+1, n):
                    for cc in range(ord('a'), ord('a')+k):
                        cj = chr(cc)
                        if valid_at(j, cj):
                            s_list[j] = cj
                            break
                # return joined
                return "".join(s_list)
            # restore and continue
            # s_list[i] = orig  # will be overwritten
        return ""
