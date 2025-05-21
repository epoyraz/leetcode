class Solution:
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        n = len(mountain)
        peaks = []
        # iterate from 1 to n-2 (cannot consider first or last element)
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
