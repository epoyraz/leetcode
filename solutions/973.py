class Solution:
    def movesToStamp(self, stamp, target):
        stamp_len, target_len = len(stamp), len(target)
        s = list(target)
        res = []
        visited = [False] * (target_len - stamp_len + 1)
        total_replaced = [0]  # use list to make it mutable in nested function

        def can_stamp(pos):
            changed = False
            for i in range(stamp_len):
                if s[pos + i] == '?':
                    continue
                if s[pos + i] != stamp[i]:
                    return False
                changed = True
            return changed

        def do_stamp(pos):
            for i in range(stamp_len):
                if s[pos + i] != '?':
                    s[pos + i] = '?'
                    total_replaced[0] += 1

        while total_replaced[0] < target_len:
            stamped_this_round = False
            for i in range(target_len - stamp_len + 1):
                if not visited[i] and can_stamp(i):
                    do_stamp(i)
                    visited[i] = True
                    res.append(i)
                    stamped_this_round = True
            if not stamped_this_round:
                return []

        return res[::-1]
