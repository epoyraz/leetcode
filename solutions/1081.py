class Solution:
    def videoStitching(self, clips, time):
        clips.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        curr_end = 0
        i = 0
        n = len(clips)
        while curr_end < time:
            furthest = curr_end
            while i < n and clips[i][0] <= curr_end:
                furthest = max(furthest, clips[i][1])
                i += 1
            if furthest == curr_end:
                return -1
            res += 1
            curr_end = furthest
        return res
