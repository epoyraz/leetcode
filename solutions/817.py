class MyHashMap(object):
    def __init__(self):
        # key range is [0, 10^6], so we allocate size 10^6+1
        self.size = 10**6 + 1
        # Initialize all entries to -1, meaning "no mapping"
        self.data = [-1] * self.size

    def put(self, key, value):
        """
        Insert a (key, value) pair into the HashMap.
        If the key already exists, update its value.
        """
        self.data[key] = value

    def get(self, key):
        """
        Return the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key.
        """
        return self.data[key]

    def remove(self, key):
        """
        Remove the mapping for the specified key, if it exists.
        """
        self.data[key] = -1
