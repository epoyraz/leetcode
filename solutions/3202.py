from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times):
        d = defaultdict(list)
        for name, t in access_times:
            hh, mm = int(t[:2]), int(t[2:])
            d[name].append(hh * 60 + mm)

        res = []
        for name, times in d.items():
            times.sort()
            j = 0
            for i in range(len(times)):
                # shrink window so that difference â¤ 59 minutes
                while times[i] - times[j] > 59:
                    j += 1
                if i - j + 1 >= 3:
                    res.append(name)
                    break
        return res
