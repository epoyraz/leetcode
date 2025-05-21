class Robot:
    def __init__(self, width, height):
        """
        Pre-compute the perimeter cycle.
        After the first move, the robot keeps looping over this cycle:
          length L = 2*width + 2*height â 4
        """
        self.cycle = []

        # 1) bottom edge, going East
        for x in range(1, width):
            self.cycle.append((x, 0, "East"))

        # 2) right edge, going North
        for y in range(1, height):
            self.cycle.append((width - 1, y, "North"))

        # 3) top edge, going West
        for x in range(width - 2, -1, -1):
            self.cycle.append((x, height - 1, "West"))

        # 4) left edge, going South
        for y in range(height - 2, -1, -1):
            self.cycle.append((0, y, "South"))

        self.L = len(self.cycle)      # perimeter length
        self.t = 0                    # total steps taken so far

    # ----------------------------------------------------------

    def step(self, num):
        """Move forward num steps."""
        self.t += num                 # just accumulate â Python int is unbounded

    # ----------------------------------------------------------

    def getPos(self):
        """Return [x, y] of current cell."""
        if self.t == 0:
            return [0, 0]             # still at the start
        x, y, _ = self.cycle[(self.t - 1) % self.L]
        return [x, y]

    # ----------------------------------------------------------

    def getDir(self):
        """Return current facing direction."""
        if self.t == 0:
            return "East"
        return self.cycle[(self.t - 1) % self.L][2]
