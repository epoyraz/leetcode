class MyHashSet(object):

    def __init__(self):
        # Keys are in [0, 10^6], so we can use a fixed-size bytearray
        self.data = bytearray(10**6 + 1)

    def add(self, key):
        # Mark presence by setting to 1
        self.data[key] = 1

    def remove(self, key):
        # Mark absence by setting back to 0
        self.data[key] = 0

    def contains(self, key):
        # Return True if marked present
        return self.data[key] == 1
