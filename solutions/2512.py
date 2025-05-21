class LUPrefix:
    def __init__(self, n):
        # Track which videos have been uploaded
        self.uploaded = [False] * (n + 2)
        # Pointer to the smallest missing video in the prefix
        self.curr = 1
        self.n = n

    def upload(self, video):
        # Mark this video as uploaded
        self.uploaded[video] = True
        # Advance curr while the next video is uploaded
        while self.curr <= self.n and self.uploaded[self.curr]:
            self.curr += 1

    def longest(self):
        # All videos 1..curr-1 have been uploaded
        return self.curr - 1
