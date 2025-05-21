class Solution:
    MOD = 10**9 + 7

    def count_upto(self, s, min_sum, max_sum):
        n = len(s)
        dp_curr = [[0, 0] for _ in range(max_sum + 1)]
        dp_curr[0][1] = 1

        for ch in s:
            digit = ord(ch) - 48
            dp_next = [[0, 0] for _ in range(max_sum + 1)]
            for sm in range(max_sum + 1):
                cnt0, cnt1 = dp_curr[sm]
                if cnt0:
                    for d in range(10):
                        sm2 = sm + d
                        if sm2 > max_sum:
                            break
                        dp_next[sm2][0] = (dp_next[sm2][0] + cnt0) % self.MOD
                if cnt1:
                    for d in range(digit):
                        sm2 = sm + d
                        if sm2 > max_sum:
                            break
                        dp_next[sm2][0] = (dp_next[sm2][0] + cnt1) % self.MOD
                    sm2 = sm + digit
                    if sm2 <= max_sum:
                        dp_next[sm2][1] = (dp_next[sm2][1] + cnt1) % self.MOD
            dp_curr = dp_next

        res = 0
        for sm in range(min_sum, max_sum + 1):
            res = (res + dp_curr[sm][0] + dp_curr[sm][1]) % self.MOD
        return res

    def decrement_str(self, s):
        lst = list(s)
        i = len(lst) - 1
        while i >= 0:
            if lst[i] == '0':
                lst[i] = '9'
                i -= 1
            else:
                lst[i] = chr(ord(lst[i]) - 1)
                break
        if lst and lst[0] == '0':
            lst.pop(0)
        return ''.join(lst)

    def count(self, num1, num2, min_sum, max_sum):
        cnt2 = self.count_upto(num2, min_sum, max_sum)
        num1m1 = self.decrement_str(num1)
        cnt1 = self.count_upto(num1m1, min_sum, max_sum) if num1m1 else 0
        return (cnt2 - cnt1) % self.MOD
