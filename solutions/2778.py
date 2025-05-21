class FrequencyTracker(object):
    def __init__(self):
        # count[number] = current frequency of number
        self.count = {}
        # freq_map[f] = number of elements that appear exactly f times
        self.freq_map = {}

    def add(self, number):
        # old frequency
        old = self.count.get(number, 0)
        # decrement old freq count
        if old > 0:
            self.freq_map[old] -= 1
        # new frequency
        new = old + 1
        self.count[number] = new
        # increment new freq count
        self.freq_map[new] = self.freq_map.get(new, 0) + 1

    def deleteOne(self, number):
        old = self.count.get(number, 0)
        if old == 0:
            return  # nothing to delete
        # decrement old freq count
        self.freq_map[old] -= 1
        # new frequency
        new = old - 1
        if new > 0:
            self.count[number] = new
            # increment the new frequency count
            self.freq_map[new] = self.freq_map.get(new, 0) + 1
        else:
            # remove the number entirely
            del self.count[number]

    def hasFrequency(self, frequency):
        # return True if any number has exactly `frequency` occurrences
        return self.freq_map.get(frequency, 0) > 0
