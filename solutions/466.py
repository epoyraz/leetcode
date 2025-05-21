class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if n1 == 0:
            return 0

        index = 0  # index in s2
        s2cnt = 0  # how many times s2 matched
        recall = dict()
        s1cnt = 0  # how many s1 blocks processed

        while s1cnt < n1:
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        s2cnt += 1
            s1cnt += 1

            if index in recall:
                # Loop detected
                s1cnt_prev, s2cnt_prev = recall[index]
                pre_loop_s1cnt = s1cnt_prev
                pre_loop_s2cnt = s2cnt_prev

                loop_s1cnt = s1cnt - s1cnt_prev
                loop_s2cnt = s2cnt - s2cnt_prev

                loops = (n1 - pre_loop_s1cnt) // loop_s1cnt
                s1cnt = pre_loop_s1cnt + loops * loop_s1cnt
                s2cnt = pre_loop_s2cnt + loops * loop_s2cnt
                break
            else:
                recall[index] = (s1cnt, s2cnt)

        # Remaining s1 blocks after loop
        rest_s2cnt = 0
        index = index
        for _ in range(s1cnt, n1):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        rest_s2cnt += 1

        return (s2cnt + rest_s2cnt) // n2
