class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        waiting = 0
        total_boarded = 0
        best_profit = 0
        best_rotation = -1
        profit = 0

        # 1) process the first n rotations with arrivals
        for i, arrive in enumerate(customers, start=1):
            waiting += arrive
            # board up to 4
            boarded = waiting if waiting < 4 else 4
            waiting -= boarded
            total_boarded += boarded

            profit = total_boarded*boardingCost - i*runningCost
            if profit > best_profit:
                best_profit = profit
                best_rotation = i

        # 2) any leftover waiting?
        #    If sending 4 every extra rotation is still profitable...
        delta = 4*boardingCost - runningCost
        if waiting > 0 and delta > 0:
            # how many full 4âperson rotations?
            full = waiting // 4
            rem  = waiting % 4

            # profit after all full rotations
            profit_full_end = profit + full * delta
            rot_full_end   = len(customers) + full
            if profit_full_end > best_profit:
                best_profit = profit_full_end
                best_rotation = rot_full_end

            # consider one final partial rotation (if any remain)
            if rem:
                profit_partial_end = profit_full_end + rem*boardingCost - runningCost
                rot_part = rot_full_end + 1
                if profit_partial_end > best_profit:
                    best_profit = profit_partial_end
                    best_rotation = rot_part

        return best_rotation
