class Solution(object):
    def checkInclusion(self, s1, s2):
        m, n = len(s1), len(s2)
        if m > n:
            return False
        # frequency arrays
        cnt1 = [0]*26
        cnt2 = [0]*26
        for i in range(m):
            cnt1[ord(s1[i]) - 97] += 1
            cnt2[ord(s2[i]) - 97] += 1
        if cnt1 == cnt2:
            return True
        for i in range(m, n):
            cnt2[ord(s2[i]) - 97] += 1
            cnt2[ord(s2[i-m]) - 97] -= 1
            if cnt1 == cnt2:
                return True
        return False
