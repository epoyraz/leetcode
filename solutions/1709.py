from collections import defaultdict

class Solution:
    def alertNames(self, keyName, keyTime):
        # Map each worker to their list of access times (in minutes)
        times_map = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            minutes = int(t[:2]) * 60 + int(t[3:])
            times_map[name].append(minutes)
        
        alerted = []
        # Check each worker's sorted times for any 3 within a 60âminute window
        for name, times in times_map.items():
            times.sort()
            # Sliding window of size 3: check if times[i+2] - times[i] <= 60
            for i in range(len(times) - 2):
                if times[i+2] - times[i] <= 60:
                    alerted.append(name)
                    break
        
        return sorted(alerted)
