class Solution:
    def splitMessage(self, message, limit):
        m = len(message)
        # Precompute sum_len[i] = sum of digit-lengths of numbers 1..i
        sum_len = [0] * (m + 1)
        for i in range(1, m + 1):
            sum_len[i] = sum_len[i - 1] + len(str(i))

        # Find the minimal b for which total capacity >= m
        b_found = 0
        for b in range(1, m + 1):
            len_b = len(str(b))
            # If even the smallest cap (with len_i = len_b) is negative, no larger b will work
            if limit < 3 + 2 * len_b:
                break

            # total_cap = sum_{i=1..b} [limit - (3 + len(i) + len_b)]
            # = b*(limit - 3 - len_b) - sum_len[b]
            total_cap = b * (limit - 3 - len_b) - sum_len[b]
            if total_cap >= m:
                b_found = b
                break

        if b_found == 0:
            return []

        # Build the parts using b_found
        parts = []
        sb = str(b_found)
        len_b = len(sb)
        idx = 0
        for i in range(1, b_found + 1):
            si = str(i)
            suffix = "<" + si + "/" + sb + ">"
            cap = limit - len(suffix)
            take = min(cap, m - idx)
            parts.append(message[idx : idx + take] + suffix)
            idx += take
            if idx >= m:
                break

        return parts
