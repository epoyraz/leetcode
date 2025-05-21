class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        current_time = 0
        total_wait = 0
        
        for arrival, prep in customers:
            if current_time <= arrival:
                current_time = arrival + prep
                total_wait += prep
            else:
                total_wait += (current_time + prep - arrival)
                current_time += prep
        
        # ensure float division even in Python2
        return total_wait * 1.0 / len(customers)
