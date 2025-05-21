from collections import defaultdict
import bisect

class TweetCounts:
    def __init__(self):
        # Map each tweetName to a sorted list of timestamps
        self.times = defaultdict(list)

    def recordTweet(self, tweetName, time):
        # Insert time into the sorted list
        lst = self.times[tweetName]
        bisect.insort(lst, time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        # Determine chunk size
        if freq == "minute":
            delta = 60
        elif freq == "hour":
            delta = 3600
        else:  # "day"
            delta = 86400

        # Number of chunks in [startTime, endTime]
        num_chunks = (endTime - startTime) // delta + 1
        counts = [0] * num_chunks

        lst = self.times.get(tweetName, [])
        if not lst:
            return counts

        # Find the slice of timestamps within [startTime, endTime]
        lo = bisect.bisect_left(lst, startTime)
        hi = bisect.bisect_right(lst, endTime)

        # Bucket each timestamp into its chunk
        for t in lst[lo:hi]:
            idx = (t - startTime) // delta
            counts[idx] += 1

        return counts
