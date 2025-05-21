class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()
        n = len(passengers)
        j = 0
        
        # simulate boarding on each bus
        for depart in buses:
            cnt = 0
            while j < n and passengers[j] <= depart and cnt < capacity:
                j += 1
                cnt += 1
        
        last_depart = buses[-1]
        
        # if last bus isn't full, we can arrive exactly at its departure
        if cnt < capacity:
            candidate = last_depart
        else:
            # otherwise, one before the last boarded passenger
            candidate = passengers[j-1] - 1
            
            # avoid any run of consecutive arrivals at the end of that bus
            l = j - cnt
            r = j - 1
            arr = passengers
            lo, hi = l, r
            # binary-search for the start of the maximal consecutive suffix ending at r
            while lo < hi:
                mid = (lo + hi) // 2
                # if arr[mid..r] are fully consecutive integers...
                if arr[r] - arr[mid] == r - mid:
                    hi = mid
                else:
                    lo = mid + 1
            # now arr[lo..r] is a consecutive block, so we must step before arr[lo]
            if candidate >= arr[lo]:
                candidate = arr[lo] - 1
        
        # finally, ensure we don't clash with *any* passenger arrival
        import bisect
        pos = bisect.bisect_left(passengers, candidate)
        while pos >= 0 and pos < n and passengers[pos] == candidate:
            candidate -= 1
            pos -= 1
        
        return candidate
