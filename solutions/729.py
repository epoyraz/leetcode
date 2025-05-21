class MyCalendar(object):
    def __init__(self):
        # List to store booked events as (start, end) tuples
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # Check for overlap with any existing event
        for s0, e0 in self.events:
            # Overlap exists if start < e0 and s0 < end
            if start < e0 and s0 < end:
                return False
        # No overlap; add the new event
        self.events.append((start, end))
        return True
